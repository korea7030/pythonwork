# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:11:36 2015

@author: Administrator
"""

import numpy as np
from sklearn import datasets 
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

result = []
score = []

k_range = range(8,20) 

iris= datasets.load_iris()
X,y = iris.data, iris.target 

for k in k_range :
    result.append(k)
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X,y)
    print('k is %d, score is %f' %(k, knn.score(X,y)))
    score.append(knn.score(X,y))

    ## score 점수
    plt.plot(score)
