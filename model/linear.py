import sys
from sklearn.metrics import roc_auc_score
import numpy as np
import pickle

X=[]
Y=[]
L=[]
trainf=open(sys.argv[1])
for l in trainf.readlines():
    sl = l.strip().split()
    L.append(sl[0])
    Y.append(int(sl[1]))
    xx=map(float,sl[2:])
    X.append(xx)

coef=np.array([ 0.15,0.3,0.25,0.15,0.15])
YY=np.dot(X,coef)
print roc_auc_score(Y,YY), coef

del X

X=[]
L=[]
testf=open(sys.argv[2])
for l in testf.readlines():
    sl = l.strip().split()
    L.append(sl[0])
    xx=map(float,sl[1:])
    X.append(xx)
Y=np.dot(X,coef)
outf=open(sys.argv[3], 'w')
outf.write('projectid,is_exciting\n')
for i in xrange(0, len(Y)): 
    outs='%s,%.8f\n'%(L[i], Y[i])
    outf.write(outs)
