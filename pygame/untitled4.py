# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 21:17:57 2016

@author: Administrator
"""

class Num1:
    def __init__(self, a):
        self.num = a

class Num2:
    def __init__(self, a):
        self.num = a
    def __add__(self,a):
        self.num += a
    def __sub__(self,a):
        self.num -= a

n1 = Num1(40)
n1+40
print n1.num

n2 = Num2(20)
n2+40
print n2.num


        