# -*- coding: utf-8 -*-

def hap(x,y) :
    return x+y

hap(10,20)
## 30

## lambda 
(lambda x,y:x+y)(10,20)
## 30

## map(function, list)
map(lambda x:x **2, range(5))
## 0,1,4,9,16

list(map(lambda x:x**2, range(5)))
## 0,1,4,9,16

## reduce(function, sequence data)
reduce(lambda x,y:x+y, [0,1,2,3,4])
## ((((0+1)+2)+3)+4)+5 

## filter(func, list)
filter(lambda x:x < 5, range(10))
## 0,1,2,3,4


filter(lambda x: x%2, range(10))
## 1,3,5,7,9
## 2로나눈 나머지가 1인것만 출력

x = 'banana'
x[0] 
x[2:4]
x[3:]

x[0] = 'n'

x

x = 'n'+x[1:]
x


## list 
prime = [2,3,7,11]
prime.append(5)
prime

prime.sort()
prime

del prime[4]  ## 4번째 요소 삭제
prime

prime[0] = 1
prime


orders = ['potato', ['pizza', 'cake', 'salad'], 'hamburger']

orders[1]
# [pizza, cake, salad]

## 문자열을 목록으로 
characters = [] 
sentence = 'Be happy!'

for char in sentence:
    characters.append(char)
    
print(characters)

## 성적표 
chulsu = [90,85,70]
younghee = [88,79,92]
yong = [100,100,100]
minsu = [90, 60,70]

students = [chulsu, younghee, yong, minsu]

for scores in students:
    total = 0
    for s in scores:
        total = total + s
    average = total / 3 
    print(scores, total, average)
    

## tuples
c = 10
d = 20
c,d=d,c
print c,d
## 20,10

def magu_print(x,y,*rest):
    print x,y,rest

## 2개 이상만 정의해주면 알아서 나머지는 묶어줌    
magu_print(1,2,3,5,6,7,9,10)

t = ('a','b','c')    

p = (1,2,3)
q = p[:1] + (5,) + p[2:]

q
## 1,5,3

r = p[:1] , 5, p[2:]
r

p= (1,2,3)

## tuple to list 
q = list(p)
q

## list to tuple
r = tuple(q)
r

## dictionary
# key, value 로 구성
dic = {}
dic['dictionary'] = '1. A reference book containing an ...'

dic['python'] = 'And of various nonvnomous snakes of the ...'
dic['dictionary']

dic

## key 값으로 조회
family = {'boy':'chi', 'girl':'kim', 'baby':'chi'}
family
family.keys()

family.values()

'boy' in family
'syster' in family

