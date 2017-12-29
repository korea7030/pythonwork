# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:43:51 2015

@author: Administrator
"""

import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.cross_validation import KFold

iris = datasets.load_iris()
X, y = iris.data, iris.target

folds = 5
kf = KFold(len(y), n_folds=folds, indices=True)

k_range = range(3, 20)
score_means = []

for k in k_range:
    test_scores = []
    knn = KNeighborsClassifier(n_neighbors=k)
    for train, test in kf:
        X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
        knn.fit(X_train, y_train)
        score = knn.score(X_test, y_test)
        test_scores.append(score)

    score_means.append(sum(test_scores) / folds)
    print('K is %d, test score is mean %f' % (k, sum(test_scores) / folds))


plt.plot(k_range, score_means)
plt.legend(['K value'], loc='upper right')
plt.show()
