# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:16:50 2015

@author: Administrator
"""

from sklearn import datasets 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
# from sklearn.svm import SVC
# from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from sklearn.grid_search import GridSearchCV 

if __name__ == '__main__':
    
    iris= datasets.load_iris()
    X,y = iris.data, iris.target 
    
    kf = KFold(len(y), n_folds=5)
    
    ## KNN
    estimators = [('pca', PCA()), ('knn', KNeighborsClassifier())]
    parameters = {'pca__n_components':(2, 3), 'knn__n_neighbors':
    (6,7,8,9,10,11,12,13), 'knn__weights':('uniform', 'distance')}
    
    ## SVM
    #estimators = [('pca', PCA()), ('svm', SVC())]
    #parameters = {'pca__n_components':(2, 3), 'svm__C':(0.4, 1, 1.5, 2, 3)}
        
    ## LogisticRegression
    #estimators = [('pca', PCA()), ('lr', LogisticRegression())]
    #parameters = {'pca__n_components':(2, 3), 'lr__penalty':( 'l1', 'l2')}
    
    pipeline = Pipeline(estimators)
    print(pipeline)
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1, cv=kf)
    print("Performing grid search...")
    print("pipeline:", [name for name, _ in pipeline.steps])
    grid_search.fit(X, y)
    print("Best score: %0.3f" % grid_search.best_score_)
    print("Best parameters set:")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))
