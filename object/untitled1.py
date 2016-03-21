# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:22:17 2016

@author: Administrator
"""

class C1:
    def name():
        print "C1"

class C2:
    def name():
        print "C2"
    def __str__(self):              
        msg= "나는 C2입니다."
        return msg
        

c1 = C1()
c2 = C2()

print "C1 print : ",c1
print "C2 print : ",c2