# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:44:10 2016

@author: Administrator
"""

class A:
    def __init__(self, a):
        self.a = a
    def call(self):
        print "A의 call() 함수 실행"
    def __str__(self):
        return "",a

class B(A):
    def call(self):
        print "B의 call() 함수 실행"

class C(A):
    def call(self):
        print "C의 call() 함수 실행"

a = A(1)
b = B(2)
c = C(3)

a.call()
b.call()
c.call()
print a.a
print b.a
print c.a