# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:28:48 2015

@author: Administrator
"""

import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split


iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

k_range = range(3, 20)
train_scores = []
test_scores = []


for k in k_range:

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    train_score = knn.score(X_train, y_train)
    train_scores.append(train_score)
    test_score = knn.score(X_test, y_test)
    test_scores.append(test_score)

    print('k is %d, train_score=%f, test_score = %f' % (k, train_score, test_score))

print('Train score is mean %f' % (sum(train_scores) / len(k_range)))
print('Test score is mean %f' % (sum(test_scores) / len(k_range)))

plt.plot(k_range, train_scores, 'b')
plt.plot(k_range, test_scores, 'g')
plt.legend(['train_score', 'test_score'], loc='right')
plt.show()
