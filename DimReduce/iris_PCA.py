# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:41:15 2015

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.lda import LDA 
from sklearn.decomposition import FactorAnalysis 

iris = load_iris()
X,y = iris.data, iris.target
target_names = iris.target_names

## PCA(주성분분석)
pca= PCA(n_components=2)
X_r = pca.fit_transform(X)

plt.figure()

for c,i,target_name in zip("rgb", [0,1,2], target_names) :
    plt.scatter(X_r[y==i,0], X_r[y==i, 1], c=c, label=target_name)

plt.legend(loc="best")
plt.title('PCA of IRIS dataset')

## LDA(선형판별분석)
lda = LDA(n_components=2)
X_r2 = lda.fit(X,y).transform(X)

plt.figure()
for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], c=c, label=target_name)
plt.legend(loc="best")
plt.title('LDA of IRIS dataset')

##FA(요인분석)
fa = FactorAnalysis(n_components=2)
X_r3 = fa.fit_transform(X)

plt.figure()
for c, i, target_name in zip("rbg", [0,1,2], target_names):
    plt.scatter(X_r3[y==i,0], X_r[y==i,1], c=c, label=target_name)
plt.legend(loc='best')
plt.title('FA of IRIS dataset')


