# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:17:32 2015

@author: Administrator
"""

import numpy as np
from sklearn import datasets 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris= datasets.load_iris()
X,y = iris.data, iris.target 

knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X,y)

print(accuracy_score(knn.predict(X),y))
