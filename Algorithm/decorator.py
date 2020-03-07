# -*- coding: utf-8 -*-
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print('dispaly 함수가 실행됐습니다.')


decorated_display = decorator_function(display)
decorated_display()

############################################################


def decorator_function2(original_function):
    def wrapper_function(*args, **kwargs):
        print('{} 함수가 호출되기 전입니다.'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function2
def display_1():
    print('display_1 함수가 실행됐습니다.')


@decorator_function2
def display_info(name, age):
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))


display_1()
print()
display_info('John', 25)

###############################################################


class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기 전 입니다.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display4():
    print('display4 함수가 호출되었습니다.')


@DecoratorClass
def display_info2(name, age):
    print('display_info2({}, {}) 함수가 실행됐습니다.'.format(name, age))


display4()
print()
display_info2('John', 25)