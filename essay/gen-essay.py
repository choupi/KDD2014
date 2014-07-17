import csv
import re
import math

def mexist(c,s):
    if c in s: return '1'
    else: return '0'

def log_trans(s):
    try:
        ss=math.log(float(s)+1)
        return '%f %f'%(ss,ss*ss)
    except: return '0 0'
    return '0 0'

bd={}
f=open('badword.txt')
for l in f.readlines():
    sl=l.split()
    bd[sl[0]]=sl[2]

gd={}
f=open('goodword.txt')
for l in f.readlines():
    sl=l.split()
    gd[sl[0]]=sl[2]

f=open('essays.csv')
c=csv.reader(f)
for r in c:
    #print r[0],r[3],r[4],r[5]
    #sl=re.split('\W+',r[3])
    #sl+=re.split('\W+',r[5])
    #g=0
    #b=0
    #sl=set(sl)
    #for w in sl:
    #    w=w.lower()
    #    if w in gd: g+=1
    #    if w in bd: b+=1
    #print r[0],log_trans(len(r[3])),log_trans(len(r[5])),mexist('!',r[2]),mexist(':',r[2]),mexist('?',r[3]),mexist('http',r[2]),g,b
    #print r[0],log_trans(len(r[3])),log_trans(len(r[5])),mexist('!',r[2]),mexist(':',r[2]),mexist('?',r[3]),mexist('http',r[3]),mexist('http',r[5])
    print r[0],log_trans(len(r[5])),mexist('!',r[2]),mexist(':',r[2]),mexist('?',r[3])

