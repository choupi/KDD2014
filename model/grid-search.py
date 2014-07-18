import sys
from sklearn.metrics import roc_auc_score,mean_absolute_error,r2_score,mean_squared_error
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

md=[0,0.2,0.25,0.3,0.35,0.4,0.5,0.75,0.8]
rd=[0,0.05,0.1,0.2,0.25,0.3,0.35]
kd=[0,0.05,0.1,0.2,0.25,0.3,0.35]
for m in md:
 for mm in rd:
  for r in rd:
   for k in kd:
    if 1-m-r-k-mm < -0.05: continue
    coef=np.array([k,1-m-r-k-mm,m,r,mm])
    YY=np.dot(X,coef)
    print roc_auc_score(Y,YY),mean_absolute_error(Y,YY), mean_squared_error(Y,YY),r2_score(Y,YY), coef

del X
exit(0)

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
