from bs4 import BeautifulSoup
import urllib.request
import random

url='http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts'
user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.44 Safari/537.36 OPR/24.0.1558.25 (Edition Next)'
myheader={'User-Agent':user_agent,'Host':'www.aflcio.org','GET':url}
req=urllib.request.Request(url,headers=myheader)
fh=urllib.request.urlopen(req).read()
soup = BeautifulSoup(fh,'html.parser')
#print(soup.prettify()[28700:30500])
letters=soup.find_all('div',class_='ec_statements')
#print (letters[0])
prefix='www.aflcio.org'
lobbying={}
for item in letters:
	lobbying[item.a.get_text()]={}
	lobbying[item.a.get_text()]['link']=prefix+item.a['href']
	lobbying[item.a.get_text()]['date']=item.find(id='legalert_date').get_text()
for item in lobbying.keys():
    print(item + ": " + "\n\t" + "link: " + lobbying[item]["link"] + "\n\t" + "date: " + lobbying[item]["date"] + "\n\n" )