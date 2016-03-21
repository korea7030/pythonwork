# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 09:10:15 2016

@author: Administrator
"""
## 변수 할당

age = 19 # 변수 
print(type(age)) # age의 type알기
print(age) # age 변수 출력

## 연산자(+,-,*,/,//,%)
1+1
1*2
2/1
2//1
2%1

## 문자열
"1" * 3 ## 출력가능
"1" + 3 ## 출력 불가능

## % 연산자를 이용한 출력
print("올해는 몇년도 인가요?")
print("%d 년 입니다. " % 2016)  ## d : decimal(숫자형)

"%s 년 입니다." "2016"

a = "hello"
b = "world"
print("%0.3s %s" % (a,b))

## format 함수(치환자)
print("올 해는 {0}년 {1}월 입니다." .format(2016,3)) ## {0} : 2016, {1} : 3 

## 조건문 
if age >= 20:
    print ("성인")
else:
    print ("미성년")


#### 반복문
## for 문 
for item in range(4): # range 0~4 까지
    print (item)

for item in range(0,4,2): # 증가값 추가한 경우
    print (item)


## enumerate
s = "statement"
for i, x in enumerate(s): # 해당 변수의 index까지 출력(unpacking)
    print (i,x)

for i,x in enumerate(12345): # 숫자형은 반복할 수 없다.
    print (i,x)

dir("python") # 객체의 메소드 확인

universities = "kookmin university"
universities.split()

## strip : 문자의 양 옆 공백 및 특정문자열 제거
print("   kookmin    university".strip())
print("kookmin".strip("n") )

#### Data Structure
## tuple (변경 불가능)
obj = (1,2,3)
print obj 
del obj(3) 

## list
cities = ['Seoul', 'Tokyo', 'New Work']
cities

cities.append("BuSan") # 뒤에만 추가
cities.insert(3,"LA") # 원하는 위치에 추가
cities.remove("BuSan") # BuSan 제거
cities.append(["DaeJeon", "Yokohama"]) # list에 list도 추가 가능
cities.append(1) # 다른 데이터 타입도 가능
cities

## Dictionary(Key, value 형식)
final_exam = {"math":100, "English":90}
print (final_exam) ## 순서는 상관없음. key로 value를 찾는다. 
final_exam.get("math") 

singer = {"Talyor swift" : 
            {"album": 
                {"1st_album" : ['a','b','c'], "2nd_album" : ['a2','b2']}
            }
         }   

print (singer)

print (singer.get("Talyor swift"))

singer['Talyor swift']['album'] # indexing 이 가능

