# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 21:31:59 2016

@author: Administrator
"""

class Rectangle:
    def __init__(self, x,y):
        self.high = x
        self.bott = y
    def getArea(x,y):
        pass

class Square(Rectangle):
    def getArea(self):
        area = self.high*self.bott
        return str(area)

class Triangle(Rectangle):
    def getArea(self):
        area = (self.high*self.bott)*0.5
        return str(area)

Square = Square(4,5)
Triangle = Triangle(4,5)

print "사각형 : "+Square.getArea()
print "삼각형 : "+Triangle.getArea()