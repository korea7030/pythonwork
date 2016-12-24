import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.externals.six import StringIO
# import pydot
import pydotplus


## data 임포트
iris = load_iris()

## data 확인
print (iris.feature_names)
print (iris.target_names)
print (iris.data[0])

test_idx = [0,50,100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# test data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# model 실행
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print (test_target)
print (clf.predict(test_data)) # 예측 라벨

# 시각화 코드(error)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf('iris.pdf')

print (test_data[1], test_target[1])
print (iris.feature_names, iris.target_names)