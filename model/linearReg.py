import sys
from sklearn.linear_model import LinearRegression
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

#print X
clf = LinearRegression(normalize=True)
clf = clf.fit(X, Y)
#print clf
#scores = cross_val_score(clf, X, Y)
#print scores
#print clf.score(X,Y)
print clf.coef_

if len(sys.argv)>4:
    Y=clf.predict_proba(X)
    tf=open(sys.argv[4], 'w')
    tf.write('projectid,is_exciting\n')
    for i in xrange(0, len(Y)): 
        outs='%s,%.8f\n'%(L[i], Y[i][1])
        tf.write(outs)
    tf.close()
del X

pf=open('clf-logReg.pkl','w')
s = pickle.dump(clf, pf)
pf.close()

X=[]
L=[]
testf=open(sys.argv[2])
for l in testf.readlines():
    sl = l.strip().split()
    L.append(sl[0])
    xx=map(float,sl[1:])
    X.append(xx)
Y=clf.predict(X)
outf=open(sys.argv[3], 'w')
outf.write('projectid,is_exciting\n')
for i in xrange(0, len(Y)): 
    outs='%s,%.8f\n'%(L[i], Y[i])
    outf.write(outs)
