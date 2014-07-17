import csv
import sys
import math

def teacher_prefix(s):
    if s=='Dr.': return '1'
    return '0'

def load_outcome():
    proj_dict={}
    f=open('outcomes.csv')
    outcome=csv.reader(f)
    for r in outcome:
        proj_dict[r[0]]=[r[1],r[3]]
    return proj_dict

def load_dt(pd,clm):
    g_dict={}
    projfile=open('projects.csv')
    projcsv=csv.reader(projfile)
    for r in projcsv:
        if r[clm] not in g_dict: g_dict[r[clm]]=[0,0,0,0]
        if r[0] in pd:
            if pd[r[0]][0]=='f': g_dict[r[clm]][0]+=1
            elif pd[r[0]][0]=='t': g_dict[r[clm]][1]+=1
            if pd[r[0]][1]=='f': g_dict[r[clm]][2]+=1
            elif pd[r[0]][1]=='t': g_dict[r[clm]][3]+=1
    projfile.close()
    return g_dict

def get_rate(d, v):
    rate_e=0
    rate_f=0
    if d[v][0]+d[v][1]>0: rate_e=d[v][1]/float(d[v][0]+d[v][1])
    if d[v][2]+d[v][3]>0: rate_f=d[v][3]/float(d[v][2]+d[v][3])
    return [str(rate_e), str(rate_f)]

def mexist(s):
    if s: return '1'
    return '0'

def log_trans(s):
    try:
        ss=math.log(float(s)+1)
        return '%f %f'%(ss,ss*ss)
    except: return '0 0'
    return '0 0'

def load_projects():
    #$1,$5,$6,$9,$13,$14,$15,$16,$17,$18,$20,$21,$29,$30,$31,$32
    projfile=open('projects.csv')
    projcsv=csv.reader(projfile)
    for r in projcsv:
        rr=[mexist(r[3]),r[12],r[13],r[14],r[15],r[16],r[17],r[19],r[20],
            log_trans(r[29]),log_trans(r[31]), r[32],r[33]]
        for i in xrange(0,len(rr)):
            if rr[i]=='f': rr[i]='0'
            elif rr[i]=='t': rr[i]='1'
            elif rr[i]=='': rr[i]='0'
        print r[0], ' '.join(rr)

load_projects()
