import csv
import sys
import re

def load_dummy(f):
    proj_dict={}
    f=open(f)
    for l in f.readlines():
        sl=l.strip().split('\t')
        proj_dict[sl[0]]=sl[1]
    return proj_dict

def load_projects():
    #$1,$5,$6,$9,$13,$14,$15,$16,$17,$18,$20,$21,$29,$30,$31,$32
    sd=load_dummy('state.txt')
    psd=load_dummy('subject.txt')
    pd=load_dummy('poverty.txt')
    rd=load_dummy('resource.txt')
    gd=load_dummy('grade.txt')
    md=load_dummy('month.txt')
    #yd=load_dummy('year.txt')
    td=load_dummy('tprefix.txt')
    projfile=open('projects.csv')
    projcsv=csv.reader(projfile)
    for r in projcsv:
        s=''
        if r[7] in sd: s+=sd[r[7]]+' '
        else: s+=sd['-']+' '
        if r[18] in td: s+=td[r[18]]+' '
        else: s+=td['-']+' '
        if r[21] in psd: s+=psd[r[21]]+' '
        else: s+=psd['-']+' '
        if r[23] in psd: s+=psd[r[23]]+' '
        else: s+=psd['-']+' '
        if r[26] in pd: s+=pd[r[26]]+' '
        else: s+=pd['-']+' '
        if r[25] in rd: s+=rd[r[25]]+' '
        else: s+=rd['-']+' '
        if r[27] in gd: s+=gd[r[27]]+' '
        else: s+=gd['-']+' '
        rr=re.split('\W+', r[34])
        if len(rr)>1 and rr[1] in md: s+=md[rr[1]]+' '
        else: s+=md['-']+' '
        #if rr[0] in yd: s+=yd[rr[0]]+' '
        #else: s+=yd['-']+' '
        print r[0], s

load_projects()
