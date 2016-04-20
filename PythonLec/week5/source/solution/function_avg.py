# # 사용자가 몇 개의 인수든 상관없이 모든 인수의 평균을 구하는 함수를 만들어봅시다.

# Write your code below.
def avg(*args):
	try:
		if not args:
			raise ValueError('empty value')
		else:
			print(sum(args) / len(args))
	except ValueError as e:
		print(e)

if __name__ == '__main__':
	avg()