import json
import urllib.request

url = urllib.request.urlopen("http://python-data.dr-chuck.net/comments_304585.json")
data=url.read()
js=json.loads(data.decode())


print(sum([item['count'] for item in js['comments']]))
