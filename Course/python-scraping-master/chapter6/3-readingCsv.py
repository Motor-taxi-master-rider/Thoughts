import csv
from io import StringIO
from urllib.request import urlopen

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

for row in csvReader:
	print("The album \""+row[0]+"\" was released in "+str(row[1]))
