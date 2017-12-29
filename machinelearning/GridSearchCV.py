# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:07:29 2015

@author: Administrator
"""

import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import cross_val_score, KFold, ShuffleSplit

iris = datasets.load_iris()
X, y = iris.data, iris.target

kf = KFold(len(y), n_folds=5)

k_range = range(3, 20)
parameters = {'n_neighbors': k_range}
knn_base = KNeighborsClassifier()

grid_search = GridSearchCV(knn_base, parameters, cv=kf)
grid_search.fit(X, y)
print(grid_search)
print(grid_search.best_params_)
print(grid_search.grid_scores_)
