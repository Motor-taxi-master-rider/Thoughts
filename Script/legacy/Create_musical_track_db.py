import sqlite3
import xml.etree.ElementTree as ET

conn=sqlite3.connect(r'E:\3.9.0\Python1.sqlite')
cur=conn.cursor()

cur.executescript('''
CREATE TABLE if not EXISTS Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE if not EXISTS Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE if not EXISTS  Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT
);

CREATE TABLE if not EXISTS  Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT ,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

def lookup(d, value):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == value :
            found = True
    return 'None'

fname=input('Enter file name: ')
if(len(fname)<1) :
    fname='F:\How to be a good qingnian\Learn\Python\Library.xml'

fh=ET.parse(fname)
lst=fh.findall('dict/dict/dict')
print('len=',len(lst))
for item in lst:
    #print(lookup(item,'Track ID'))
    name=lookup(item,'Name')
    artist=lookup(item,'Artist')
    album=lookup(item, 'Album')
    genre=lookup(item, 'Genre')
    len=lookup(item, 'Total Time')
    rating=lookup(item, 'Rating')
    count=lookup(item, 'Play Count')
    #print(artist,album)
    #print('------------')
    cur.execute('select count(id) from artist where name=?', (artist,))
    if cur.fetchone()[0]== 0:
        cur.execute('INSERT into artist(name) values(?) ',(artist,))
    cur.execute('select id from artist where name=?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('select count(id) from genre where name=?', (genre,))
    if cur.fetchone()[0] == 0:
        cur.execute('INSERT into genre(name) values(?) ', (genre,))
    cur.execute('select id from genre where name=?', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('SELECT count(id) FROM album WHERE artist_id=? and title=?', (artist_id,album))
    if cur.fetchone()[0] == 0:
        cur.execute('INSERT into album(artist_id,title) values(?,?) ', (artist_id,album))
    cur.execute('select id from album where artist_id=? and title=?', (artist_id,album))
    album_id=cur.fetchone()[0]

    cur.execute('SELECT count(id) FROM track WHERE title=? and album_id=? and genre_id=?', (name, album_id, genre_id))
    if cur.fetchone()[0] == 0:
        cur.execute('''INSERT INTO Track
            (title, album_id,genre_id, len, rating, count)
            VALUES ( ?, ?, ?, ?, ?,? )''',
                (name, album_id, genre_id, len, rating, count))

conn.commit()
