# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:54:15 2015

@author: Administrator
"""

import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.cross_validation import LeaveOneOut

iris = datasets.load_iris()
X, y = iris.data, iris.target

loo = LeaveOneOut(len(y))
print(loo)

knn = KNeighborsClassifier(n_neighbors=5)
scores = []

for train, test in loo:
    X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
    knn.fit(X_train, y_train)
    test_score = knn.score(X_test, y_test)

    scores.append(test_score)

print('mean score %f' % (sum(scores) / 150))
