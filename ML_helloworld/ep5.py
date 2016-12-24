from scipy.spatial import distance

def euc(a,b):
	return distance.euclidean(a,b)

class ScrappyKNN():
	''' K Nearest Neighbor 와 비슷한 형태의 KNN 클래스 구현'''

	def fit(self, X_train, Y_train):
		''' 모델 수행 함수 '''
		self.X_train = X_train
		self.Y_train = Y_train

	def predict(self, X_test):
		''' 예측함수 '''
		predictions = []
		for row in X_test:
			label = self.closest(row)
			predictions.append(label)

		return predictions

	def closest(self, row):
		''' 가까운 위치의 y값을 return '''
		best_dist = euc(row,self.X_train[0])	## 첫번째 값
		best_index = 0	## 첫번째 index

		for i in range(1, len(self.X_train)):
			'''
			첫번째 점부터 x_train 개수만큼 유클리드 거리를 통해 거리 계산을 수행
			가장 작은 distance를 나타내는 값을 return

			'''
			dist = euc(row, self.X_train[i])
			if dist < best_dist:
				best_dist = dist
				best_index = i
		return self.Y_train[best_index]

from sklearn import datasets
iris = datasets.load_iris()

# f(x) = y
X = iris.data # features
Y = iris.target # labels

# train / test data 나누기
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=.5) # 5:5

my_classifier = ScrappyKNN()	## 구현한 클래스 호출

my_classifier.fit(X_train, Y_train)	 ## train 수행
predictions = my_classifier.predict(X_test)		# test값 예측

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, predictions))
