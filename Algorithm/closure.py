# -*- coding: utf-8 -*-
def outer_func():  # 1
    message = 'Hi'  # 3

    def inner_func():  # 4
        print(message)  # 6 (free variable: 코드블럭 안에서 사용된 변수지만, 코드블럭안에 정의되지 않은 변수를 말함)

    return inner_func  # 5


my_func = outer_func()  # 2

print(my_func)  # 7
print()
print(dir(my_func))  # 8 __closure__ 속성이 있음
print()
print(type(my_func.__closure__))  # 9 tuple
print()
print(my_func.__closure__)  # 10 item 하나 존재
print()
print(my_func.__closure__[0])  # 11 cell이라는 문자열 object 존재
print()
print(dir(my_func.__closure__[0]))  # 12 cell_contents 라는 속성이 있음
print()
print(my_func.__closure__[0].cell_contents)  # 13 Hi 출력


print('-'*30)


def outer_func(tag):
    tag = tag

    def inner_func(txt):
        text = txt
        print('<{0}>{1}</{0}>'.format(tag, text))

    return inner_func


h1_func = outer_func('h1')
p_func = outer_func('p')

h1_func('h1태그의 안입니다.')
p_func('p태그의 안입니다.')
