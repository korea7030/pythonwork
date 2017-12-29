# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:14:58 2015

@author: Administrator
"""

import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier
dummy = DummyClassifier(strategy='stratified', random_state=0)

iris = datasets.load_iris()
X, y = iris.data, iris.target


dummy.fit(X, y)

print(dummy.score(X, y))
