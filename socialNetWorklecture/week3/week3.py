# -*- coding: utf-8 -*-

import os
os.getcwd()
os.chdir("C:\pythonwork\week3")

os.getcwd()

# tuple
t = (1, 'a', 'c')
l = list(t)  # tuple >> list 로 변환

t = tuple(l)  # list >> tuple 로 변환
t

# while
# a를 1부터 10까지 출력

a = 0
while a < 10:
        a = a + 1
        print a


# 1~ 10까지 합
#==============================================================================
 a= 1 
 hap = 0

     while a < 11 : 
        hap = hap + a
         print hap
        a = a+1
#==============================================================================
        
# if-elif-else

        
# for loop 
# 1~10까지 합(for문)
#==============================================================================
 a = [1,2,3,4,5,6,7,8,9,10]
 b= 0
 
 for i in a :
    b = b+i
    print b
    
#==============================================================================

# range 
# 1~ 10 까지 합
#==============================================================================
for k in range(1,11):
    c=0
    c = c+k
    print c
#==============================================================================

# dictionary for
#==============================================================================
a = {'John': 32, 'Sarah' : 13, 'Jane' : 25}
a.keys()

for key in a.keys() :
    print(a[key])
#==============================================================================
# dictinory 의 list 형태의 합계 구하기
#==============================================================================
temp = {'a':[1,2,3], 'b': [4,5,6,7], 'c':[8,9,10]}
temp.keys()
temp.values()

dichap = 0

temp['a']

for key1 in temp.keys() :
    for value in temp[key1] :
         dichap = dichap + value
        print dichap             
#==============================================================================

# function 
#==============================================================================
        # def function_name (parameter1, parameter2 ... ) : 
            # function body 
           #  return xxx
#==============================================================================


# 두 수의 합을 구하는 함수
#==============================================================================
def hap(x, y) :
    return x+y
    
hap(1,2)
#==============================================================================


# 두 수의 곱
#==============================================================================
def gob (x,y,z) :
    return x*y*z

gob(1,2,3)
#==============================================================================


# Module 
# R에서의 패키지 의미???
# 특정 기능을 사용하기 위한 집합체
#==============================================================================

import math
help(math)

# File I/O 

# 같은 디렉토리경로 내의 파일 가져오기 
f = open('age_test.txt','r')
print(f.readlines())

for line in f.readlines() :    
    age = line.strip()
    print(age)
