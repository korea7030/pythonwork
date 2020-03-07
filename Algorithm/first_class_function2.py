# -*- coding: utf-8 -*-
def square(x):
    return x * x


def cube(x):
    return x * x * x


def quad(x):
    return x * x * x * x


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


num_list = [1, 2, 3, 4, 5]

squares = my_map(square, num_list)
cubes = my_map(cube, num_list)
quads = my_map(quad, num_list)

print(squares)
print(cubes)
print(quads)


###############################################################


def logger(msg):
    def log_message():  # 클로저(Closure): 다른 함수의 지역변수를 그 함수가 종료된 이후에도 기억할 수 있는 함수
        print('Log: ', msg)

    return log_message


log_hi = logger('Hi')
print(log_hi)
log_hi()

del logger  # 글로벌 네임스페이스에 등록된 logger object를 지움

# logger object가 지워진 것을 확인
try:
    print(logger)
except NameError:
    print('NameError: logger는 존재하지 않습니다.')

log_hi()
