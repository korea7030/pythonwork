# -*- coding: utf-8 -*-
from __future__ import print_function
"""
Created on Sat Sep 12 10:18:10 2015

@author: Administrator
@ week2 python programming 
"""
import os  ## 경로가져오기 관련 import 
os.chdir("C:/pythonwork/week2")  ## 폴더 경로 변경
cwd = os.getcwd()   ## 현재 working directory 폴더경로 변수 받기 

#==============================================================================
# print(cwd)
#==============================================================================
x=3
type(x) ## type 확인
help(x) ## 변수나 명령어에 대한 도움말


y=0
#==============================================================================
# while - 반복문
#   ** 함수는 사용하거나 만들 시 : 로 구분
#==============================================================================
while(y < 10) :
    print(y)
    y=y+1

## 앞에서 부터 접근할때 
a = ['Python',1,5]
a[0]  # Python
a[1]  # 1
a[2]  # 5 

## list 접근 시 -로 접근이 가능(순서는 뒤에서부터)
a[-1] # 5
a[-2] # 1
a[-3] # Python 


a[0:2]  ## 마지막 element 순서는 포함되지 않음. 즉 0~(2-1)순서 까지
a[0:]   ## 앞에만 적을 경우 다 출력

x = [1,2,3,4]
x[1] ## 2 

## 넣고 싶은 위치에 값 넣기
x[1] = 'Python'

x 


y = [1,2,3,4]
dir(y) ## 구조를 보고 싶을 때??
len(y) ## list의 길이

y.append(5) ## y 부분 뒤에 하나 추가

y

y.extend([5,6])  ## list 추가(5,6이 뒤에 추가된다.)

## 그럼 길이도 달라짐
len(y)

y.insert(6, 'new') ## 6번째에 추가하는게 아니고 6번째 앞에 추가

## 학인
y 

## 해당 index의 값을 삭제 
del y[1]

y

## 해당 index를 지울 때
y.pop(1)

## 해당값을 지울 때
y.remove(4) 
y 

## 어떤값이 list에 있는지 확인 
1 in y ## false
5 in y ## true 

s= 'python'
type(s)

## indexing 이 가능
s.index("p")

len(s)

## 더하기연산 가능
h = "Hello"+"World"
h

## 출력
print(h)
h

## space를 통해 연결을 하고 싶을 때 
m = " ".join(['I','am','learning','python'])

## 단어를 쪼갤 떄 
m.split()

d = 'python programing'

d.split()

e = 'python' 

e.split('y')

## 공백문자 날리기, 원하는 문자 제거도 가능 

r = ' python  '

## 전체 공백 제거 
r.strip()

## 왼쪽공백 제거
r.lstrip()

## 오른쪽 공백 제거
r.rstrip()

## 문자열에서 찾고자 하는 문자의 위치 확인 
r.find("y")

## 시작글자의 위치와 끝나는 위치 찾기 (맞으면 true 아니면 false)
r.startswith("p")
r.endswith(" ")

## 문자열 요소 바꾸기 
r.replace('p','l')

t = '123'
t.isdigit()  ## true
t.isalpha()  ## false

type(t)

## type 변경
int(t) + 1 
type(t)

## format  지정할때

"{0} is an {1}".format("Dog", "animal")

## % 
"%s is an %s"%("Dog","animal")

## dictionary : {key:value}

dict = {'Tom' : 23, 'John' : 34, 'Bob' : 12}
dict['Tom'] ## 23
dict['Sarah'] ## 없음

dict['Sarah'] = 36

dict
dict.clear()

dict

## dictionary 의 key값 가져오기 
keys = dict.keys()
keys

## dictionary 의 value값 가져오기 
values = dict.values()
values

## 변수 자체를 지움 {} 까지 지움
del dict
dict

