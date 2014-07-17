import csv
import re

def load_outcome():
    proj_dict={}
    f=open('outcomes.csv')
    outcome=csv.reader(f)
    for r in outcome:
        proj_dict[r[0]]=[r[1],r[3]]
    return proj_dict

pd=load_outcome()
f=open('essays.csv')
c=csv.reader(f)
for r in c:
    #print r[0],r[3],r[4],r[5]
    rr=re.sub('\\[a-zA-Z]', ' ', r[3]+' '+r[5])
    sl=re.split('\W+',rr)
    sl=set(sl)
    if r[0] not in pd: continue
    e=pd[r[0]]
    for w in sl:
        w=w.lower()
        print w, ' '.join(e)

