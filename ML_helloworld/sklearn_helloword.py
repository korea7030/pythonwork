from sklearn import tree
features = [[140,1],[130,1], [150,0],[170,0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier() ## 의사결정나무 분류 사용
clf = clf.fit(features, labels) ## pattern 발견

print (clf.predict([[150,0]])) # 예측