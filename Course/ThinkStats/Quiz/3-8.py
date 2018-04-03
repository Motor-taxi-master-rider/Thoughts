import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import urllib.request
import Pmf

results = 'http://coolrunning.com/results/10/ma/Apr25_27thAn_set1.shtml'

def ReadResults(url=results):
    results = []
    conn = urllib.request.urlopen(url)
    for line in conn.fp:
        t = CleanLine(line)
        if t:
            results.append(t)
    return results

def CleanLine(line):
    t = line.split()
    if len(t) < 11:
        return None

    place, divtot, div, gun, net, pace, name, age, sex, race, loc = t[0:11]

    if not '/'.encode() in divtot:
        return None

    for time in [gun, net, pace]:
        if ':'.encode() not in time:
            return None

    return place.decode(), divtot.decode(), div.decode(), gun.decode(), net.decode(), pace.decode(),name.decode(), age.decode(), sex.decode(), race.decode(), loc.decode()

def main():
    results = ReadResults()
    print(results)

if __name__ == '__main__':
    main()
