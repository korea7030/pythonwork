# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## 함수 인자값
# *args
# 인자 이름 앞에 *를 삽입하면 함수는 여러 개의 인자를 받을 수 있다.
# *의 변수는 tueple이다.
def printa(x,y,*abc): ## *args로 쓰이기를 권장
    print(type(abc))
    for item in abc:
        print(item)

print("a","b","c","d","c","1")

## 키워드 argument
# ** 로 시작
# 사용자가 어떤 값을 입력할지 모를 때 사용
def foo(x=10, greeting="hello", **kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs.get('you'))
    print(greeting, x, kwargs.get('you'))

foo(you="Kookmin")

## 함수 문서화(Doc String)
def foo():
    """This is a foo.""" ##(Doc String : 함수가 어떤 짓을 하는지 알려줌, 함수명칭 바로 밑에 있어야함)
    return "foo"

foo()

## Doc String 보는 방법 
foo.__doc__
help(foo)

## Annotation 
# 함수의 인자값이나 return 이 어떤 자료형인지 알려줌
# 코드에 지장을 주지 않음. 
# 또다른 형태의 doc string이라 생각
def add(x:int, y:int) -> int:
    """더하기 함수입니다."""
    return x+y

## Annotations 보는 방법
help(add)
add.__annotations__

target_lst = [54,26,93,17,77,31,44,55,20] 


for i in range(len(target_lst)-1):
    # print(i)
    if (target_lst[i] > target_lst[i+1]) :
        tmp = target_lst[i+1] 
        target_lst[i+1] = target_lst[i]
        target_lst[i] = tmp

print(target_lst)

for i in range(len(target_lst)-1):
    # print(i)
    for j in range(i+1, len(target_lst)) :
        if (target_lst[i] > target_lst[j]) :
            tmp = target_lst[j] 
            target_lst[j] = target_lst[i]
            target_lst[i] = tmp

print(target_lst)