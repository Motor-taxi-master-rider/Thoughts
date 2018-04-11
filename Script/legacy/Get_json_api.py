import json
import urllib.parse
import urllib.request

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved',len(data),'characters')

    try: js = json.loads(data.decode())
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat,'lng',lng)
    location = js['results'][0]['formatted_address']
    print(location)
    place_id=js['results'][0]['place_id']
    print(place_id)
