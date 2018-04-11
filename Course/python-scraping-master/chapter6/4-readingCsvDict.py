import csv
from io import StringIO
from urllib.request import urlopen

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)

print(dictReader.fieldnames)

for row in dictReader:
    print(row)
