# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:14:21 2015

@author: Administrator
"""

from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.lda import LDA
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from sklearn.grid_search import GridSearchCV
from sklearn import datasets 

iris = datasets.load_iris()
X,y = iris.data, iris.target
kf = KFold(len(y), n_folds=10)

def grid_search_cv(estimators, parameters, title): 
    print("============================================================================") 
    print(title) 
     
    pipeline = Pipeline(estimators) 
    # print(pipeline) 
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1, cv=kf) 
#     print("Performing grid search...") 
#     print("pipeline:", [name for name, _ in pipeline.steps]) 
    tstart  = datetime.now() 
    grid_search.fit(X, y) 
    t = datetime.now() -tstart.now() 
    print("time : %f" % t.microseconds) 
    print("Best score: %0.3f" % grid_search.best_score_) 
#     print("Best parameters set:") 
#     best_parameters = grid_search.best_estimator_.get_params() 
#     for param_name in sorted(parameters.keys()): 
#         print("\t%s: %r" % (param_name, best_parameters[param_name])) 


if __name__ == '__main__':
    ## KNN 
    knn_estimators = [('knn', KNeighborsClassifier())] 
    knn_parameters = {'knn__n_neighbors':(7,), 'knn__weights':('distance',)} 
    grid_search_cv(knn_estimators, knn_parameters, 'Only KNN') 

    ## KNN with PCA 
    knn_pca_estimators = [('pca', PCA()), ('knn', KNeighborsClassifier())]
    knn_pca_parameters = {'knn__n_neighbors':(7,), 'knn__weights':('distance',)}
    grid_search_cv(knn_pca_estimators, knn_pca_parameters, 'KNN with PCA')

    # LDA
    knn_lna_estimators = [('lda', LDA()), ('knn', KNeighborsClassifier())]
    knn_fa_parameters={'knn__n_neighbors':(7,), 'knn__weights':('distance',)}    
    grid_search_cv(knn_lna_estimators, knn_fa_parameters, 'KNN with LDA')
    
    # SVM
    svm_estimators = [('svm', SVC())]
    svm_parameters = {'svm__C':(0.4, 1,1.5, 2, 3), 'svm__kernel':('linear', 'rbf', 'poly')}
    grid_search_cv(svm_estimators, svm_parameters, 'only SVM')
    
    # SVM with PCA
    svn_estimators = [('pca', PCA()), ('svm', SVC())]
    svn_parameters = {'pca__n_components':(2,3), 'svm__C':(0.4,1,1.5,2,3), 'svn__kernel':('linear', 'rbf', 'poly')}
    grid_search_cv(svm_estimators, svm_parameters, 'SVM with PCA')

    # logisticRegression
    lr_estimators = [('pca', PCA()), ('lr', LogisticRegression())]
    lr_parameters = {'pca__n_components':(2, 3), 'lr__penalty':( 'l1', 'l2')}
    grid_search_cv(lr_estimators, lr_parameters, 'LR with PCA')


    