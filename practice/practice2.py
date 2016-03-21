# -*- coding: utf-8 -*-

## 프롬프트 변경 
import sys
sys.ps1

sys.ps1 = '^^;'

## os 모듈
## os 제어(폴더 생성 및 복사) 

import os 
os.getcwd()

os.listdir('C:\\')


# String 
import string

string.capitalize('python')  ## 첫글자 대문자 

string.replace('simple','i','a')  ## 글자 변경 
string.split('break into words')  ## 분리 

## re " 문자열 다루기 
import re, glob 
p = re.compile(' .*p.*n.*')

for i in glob.glob('*'):
    m = p.match(i)
    if m:
        print m.group()

## webbrowser 

import webbrowser 
url = 'http://www.python.org/'
webbrowser.open(url)

## random 
import random
random.random()

random.randrange(1,7)
## 1이상 7미만

range(1,7)

abc = ['a','b','c','d','e']
random.shuffle(abc)
abc

random.choice(abc)


menu = '쫄면', '육계장', '비빔밥'

reload(sys)
sys


#### matplotlib 

from pylab import *

x = linspace(-1.6, 1.6, 10000)
f = lambda x: (sqrt(cos(x)) * cos(200 * x) + sqrt(abs(x)) - 0.7) * \
 pow((4-x*x),0.01)
 
 plot(x, map(f,x)) 
 show()
 
### file readline 
 f = open('C:\\Anaconda\\LICENSE_PYTHON.txt')
 f.readline()
 f.readline()
 
 for x in range(5) :
     line = f.readline()
     print(line)


users = {'kim':'3kid9', 'sun80':'393948','ljm':'py90390'}
os.getcwd()
f = open(os.getcwd()+'\\users.txt', 'w')
import pickle
pickle.dump(users, f)
f.close()

f = open('C:\\pythonwork\\practice\\users.txt')
a = pickle.load(f)
print a

