from bs4 import BeautifulSoup
import re
import sqlite3
import time
from urllib.request import urlopen

conn = sqlite3.connect(r"G:\Learn\Python\Project\wikilinks.db")
cur = conn.cursor()


def pageScraped(url):
    cur.execute("SELECT * FROM pages WHERE url = ?", (url,))
    if cur.fetchone() is None:
        return False
    page = cur.fetchone()
    if page is not None:
        cur.execute("SELECT * FROM links WHERE fromPageId = ?", (int(page[0]),))
    if cur.fetchone() is None:
        return False
    return True


def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = ?", (url,))
    print(cur.fetchone())
    if cur.fetchone() is None:
        cur.execute("INSERT INTO pages (url) VALUES (?)", (url,))
        conn.commit()
        return cur.lastrowid
    else:
        return (cur.fetchone()[0])



def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = ? AND toPageId = ?", (int(fromPageId), int(toPageId)))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (?, ?)", (int(fromPageId), int(toPageId)))
        conn.commit()


def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if not pageScraped(link.attrs['href']):
            # We have encountered a new page, add it and search it for links
            newPage = link.attrs['href']
            print(newPage)
            time.sleep(1)
            getLinks(newPage, recursionLevel + 1)
        else:
            print("Skipping: " + str(link.attrs['href']) + " found on " + pageUrl)


getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()
