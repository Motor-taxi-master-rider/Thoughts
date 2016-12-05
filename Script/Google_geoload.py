import urllib.parse
import urllib.request
import sqlite3
import json
import time
import ssl

# If you are in China use this URL:
serviceurl = "http://maps.google.cn/maps/api/geocode/json?"
#serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

conn = sqlite3.connect(r'E:\3.9.0\Python1.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

fh = open(r"F:\How to be a good qingnian\Learn\Python\M code\geodata\where.data")
count = 0
for line in fh:
    if count > 200 : break
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (address, ))

    try:
        data = cur.fetchone()[0]
        print ("Found in database ",address)
        continue
    except:
        pass

    print ('Resolving', address)
    url = serviceurl + urllib.parse.urlencode({"sensor":"false", "address": address})
    print ('Retrieving', url)
    uh = urllib.request.urlopen(url, context=scontext)
    data = uh.read()
    print ('Retrieved',len(data),'characters',data[:20].decode().replace('\n',' '))
           #.replace('\n',' '))
    count = count + 1
    try:
        js = json.loads(data.decode())
        # print js  # We print in case unicode causes an error
        #decode() is necessary
    except:
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print ('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', ( address,data ) )
    conn.commit()
    time.sleep(0.5)

print ("Run Google_geodump.py to read the data from the database so you can visualize it on a map.")
