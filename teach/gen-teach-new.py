import sys
import csv
import math

def log_trans(s):
    if s:
      #try:
        ss=math.log(float(s))
        return str(ss+ss*ss)
      #except: return '0'
    return '0'

outcomes={}

f=open('outcomes.csv')
c=csv.reader(f)
for r in c:
    outcomes[r[0]]=r

teacher={}
school={}
f=open(sys.argv[1])
for l in f.readlines():
    sl=l.strip().split()
    if sl[1] not in teacher: teacher[sl[1]]=[0,0,0,0,0,0,0,0,0,0,0,0]
    if sl[2] not in school: school[sl[2]]=  [0,0,0,0,0,0,0,0,0,0,0,0]
    teacher[sl[1]][0]+=1
    school[sl[2]][0]+=1
    #print sl[0], ' '.join(map(str,teacher[sl[1]][0:9])),
    print sl[0],' '.join(map(log_trans,[teacher[sl[1]][0],teacher[sl[1]][1],teacher[sl[1]][5],teacher[sl[1]][8],teacher[sl[1]][10]])),
    #print str(teacher[sl[1]][1]/float(teacher[sl[1]][0])),
    #print ' '.join(map(str,map(lambda x:x/teacher[sl[1]][0], teacher[sl[1]][9:]))),
    #print ' '.join(map(str,school[sl[2]][0:9])), 
    print ' '.join(map(log_trans,[school[sl[2]][0], school[sl[2]][1], school[sl[2]][5],school[sl[2]][8],school[sl[2]][10]]))
    #print str(school[sl[2]][1]/float(school[sl[2]][0])),
    #print ' '.join(map(str,map(lambda x:x/school[sl[2]][0], school[sl[2]][9:])))
    if sl[0] not in outcomes: continue
    for i in xrange(1,9):
        if outcomes[sl[0]][i]=='t': 
            teacher[sl[1]][i]+=1
            school[sl[2]][i]+=1
    for i in xrange(9,12):
        if not outcomes[sl[0]][i]: continue
        if outcomes[sl[0]][i]==0: continue
        #teacher[sl[1]][i]+=float(outcomes[sl[0]][i])
        #school[sl[2]][i]+=float(outcomes[sl[0]][i])
        teacher[sl[1]][i]+=1
        school[sl[2]][i]+=1
