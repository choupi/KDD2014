import csv
import sys

#$1,$5,$6,$9,$13,$14,$15,$16,$17,$18,$20,$21,$29,$30,$31,$32
f=open(sys.argv[1])
c=csv.reader(f)
for r in c:
    print r[int(sys.argv[2])]
