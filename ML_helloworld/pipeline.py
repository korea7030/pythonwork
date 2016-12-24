from sklearn import datasets
iris = datasets.load_iris()

# f(x) = y
X = iris.datasets # features
Y = iris.target # labels

# train / test data 나누기
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=.5) # 5:5

# 의사결정나무 수행
from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()
my_classifier.fit(X_train, Y_train)

# 예측값
predictions = my_classifier.predict(X_test)
print(predictions)

# 예측에 대한 정확도 출력
from sklearn.metrics import accuracy_score
print (accuracy_score(Y_test, predictions))