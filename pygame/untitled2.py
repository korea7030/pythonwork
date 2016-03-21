# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:30:45 2016

@author: Administrator
"""

class B1:
    var1 = 1
    def __str__(self):
        msg = "B1"
        return msg

class B2:
    def __init__(self, var1) :
        self.var1 = var1
    def __str__(self):
        msg = "B2"
        return msg
        

b1 = B1()
b2 = B2(5)

b1.var1 = 3   ## 데이터 은닉에 위배

print b1.var1

print b2.var1

