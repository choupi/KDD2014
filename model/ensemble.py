import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
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

#print X
#clf = LinearRegression()
#clf = RandomForestRegressor(n_estimators=200, max_depth=15)
#clf = ExtraTreesClassifier(n_estimators=3,bootstrap=True)
clf = GradientBoostingClassifier(n_estimators=20,max_features=None)
clf = clf.fit(X, Y)
print clf.feature_importances_ 
#print clf.oob_score_
Yp=clf.predict_proba(X)
YY=[p[1] for p in Yp]
print roc_auc_score(Y,YY),mean_absolute_error(Y,YY),mean_squared_error(Y,YY),r2_score(Y,YY)

pf=open('clfENB.pkl','w')
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
Y=clf.predict_proba(X)
outf=open(sys.argv[3], 'w')
outf.write('projectid,is_exciting\n')
for i in xrange(0, len(Y)): 
    outs='%s,%.8f\n'%(L[i], Y[i][1])
    outf.write(outs)
