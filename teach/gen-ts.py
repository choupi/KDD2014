import sys
import csv
from bisect import bisect_left
import math

def log_trans(s):
    try:
        ss=math.log(float(s)+1)
        return '%f %f'%(ss,ss*ss)
    except: return '0 0'
    return '0 0'

teach={}
school={}
f=open('proj-ts-sort.txt')
for l in f.readlines():
    sl=l.strip().split()
    if sl[1] not in teach: teach[sl[1]]=set()
    teach[sl[1]].add(sl[2])
    if sl[2] not in school: school[sl[2]]=set()
    school[sl[2]].add(sl[1])
    print sl[0], len(teach[sl[1]]), log_trans(len(school[sl[2]]))
