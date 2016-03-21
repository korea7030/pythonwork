# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 12:35:14 2015

@author: Administrator
"""
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
from sklearn.grid_search import GridSearchCV

if __name__ == '__main__':
    
    iris = load_iris()
    X,y = iris.data, iris.target
    
    iris_df = pd.DataFrame(X, columns= list(iris.feature_names))
    X, y = iris.data, iris.target  # 0.953 
    X = iris_df.iloc[:, [0,1]] # 0.733 
    # X = iris_df.iloc[:, [2,3]] # 0.947 
    kf = KFold(len(y), n_folds=10) 
    
    
    ## KNN 
    estimators = [('knn', KNeighborsClassifier())] 
    parameters = {'knn__n_neighbors':(7,), 'knn__weights':('distance',)} 
    
    
    ## SVM 
    # estimators = [('pca', PCA()), ('svm', SVC())] 
    # parameters = {'pca__n_components':(2, 3), 'svm__C':(0.4, 1, 1.5, 2, 3)} 
    
    
    ## LogisticRegression 
    # estimators = [('pca', PCA()), ('lr', LogisticRegression())] 
    # parameters = {'pca__n_components':(2, 3), 'lr__penalty':( 'l1', 'l2')} 
    
     
    pipeline = Pipeline(estimators) 
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1, cv=kf) 
    grid_search.fit(X, y) 
    print("Best score: %0.3f" % grid_search.best_score_) 
