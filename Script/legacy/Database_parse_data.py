import sqlite3
import urllib.request

conn=sqlite3.connect(r'E:\3.9.0\Python1.sqlite')
cur=conn.cursor()

cur.execute('''
drop table  if EXISTS  counts''')
cur.execute('''
create table counts(org TEXT,count INTEGER )''')

fname=input('Enter Url: ')
if(len(fname)<1):
    fname='http://www.pythonlearn.com/code/mbox.txt'
header={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
req=urllib.request.Request(fname,headers=header)
fh=urllib.request.urlopen(req)
for line in fh:
    if not line.startswith('From: '.encode()): continue
    pieces = line.split()
    org = pieces[1].split("@".encode())[1]
    print(org.decode())
    cur.execute('SELECT count FROM counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO counts (org, count)
                    VALUES ( ?, 1 )''', (org,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
                    (org,))
    # This statement commits outstanding changes to disk each
    # time through the loop - the program can be made faster
    # by moving the commit so it runs only after the loop completes
    conn.commit()

sql='select org,count from counts order by count desc limit 10'

print()
print('Counts:')
for row in cur.execute(sql):
    print(row[0],row[1])
cur.close()
