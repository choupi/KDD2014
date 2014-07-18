import sys
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
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

#print X
#clf = LinearRegression()
clf = RandomForestRegressor(n_estimators=300, max_features=None,bootstrap=True)
#clf = ExtraTreesRegressor(n_estimators=300,max_features=None,bootstrap=True)
#clf = RandomForestClassifier(n_estimators=50,bootstrap=True)
clf = clf.fit(X, Y)
print clf.feature_importances_ 
#print clf.oob_score_
YY=clf.predict(X)
print roc_auc_score(Y,YY)

pf=open('clfRF.pkl','w')
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
