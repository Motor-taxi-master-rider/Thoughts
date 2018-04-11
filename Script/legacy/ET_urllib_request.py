import urllib.request
import xml.etree.ElementTree as ET

while True:
    address=input('Enter url:')
    if len(address)<1 :
        break
    uh=urllib.request.urlopen(address)
    data=uh.read()
    print('Retrieved ',len(data),' characters')

    tree=ET.fromstring(data)
    counts=tree.findall('.//count')
    print (sum([int(item.text) for item in counts]))
