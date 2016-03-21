# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:03:10 2015

@author: Administrator
"""

import numpy as np
from sklearn import datasets 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score, KFold

iris= datasets.load_iris()
X,y = iris.data, iris.target 

kf = KFold(len(y), n_folds=5)

print(kf)

knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X,y, cv=kf)
print(sum(scores)/5)
