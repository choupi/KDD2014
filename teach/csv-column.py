import csv
import sys

f=open(sys.argv[1])
c=csv.reader(f)
for r in c:
    print r[0],r[1],r[2],r[34]
