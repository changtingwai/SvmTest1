# -*- coding: utf-8 -*-
'''
Created on 2015年9月14日

@author: bao
'''
from sklearn import svm
# X=[[0,0],[1,1]]
# y=[0,1]
# clf=svm.SVC()
# clf_model=clf.fit(X, y)
# X_test=[[-2,-2]]

# print clf.predict(X_test)
# print clf_model.support_vectors_
def LoadSet(filename):
    trainSets=[]
    trainLabel=[]
    fr=open(filename)
    for inst in fr.readlines():
#     sets=[inst.strip().split('\t') for inst in fr.readlines()]
        sets=inst.strip().split('\t')
        trainSets.append([float(sets[0]),float(sets[1])])
        trainLabel.append(float(sets[-1]))
    return trainSets,trainLabel
train1,label1=LoadSet('D:/learn/Ch02/testSetRBF.txt')
# print train1
# print label1
train2,label2=LoadSet('D:/learn/Ch02/testSetRBF2.txt')
clf=svm.SVC(kernel='rbf')
model=clf.fit(train1,label1)
result=[]
for set in train2:
    result.append(float(clf.predict(set)))
# print len(result)
# print len(label2)
errorCount=0
for i in range(len(label2)):
    if label2[i]!=result[i]:
        errorCount+=1
print "the error numbers are :%d" %errorCount
print "the error rate is :%f" %(errorCount/float(len(label2)))
    

