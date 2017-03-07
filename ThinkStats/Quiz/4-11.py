import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import brfss
import myplot

def main(name, data_dir='..'):
    resp = brfss.Respondents()
    resp.ReadRecords(data_dir)
    print(resp.records)

if __name__ == '__main__':
    main(*sys.argv)
