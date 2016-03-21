# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 21:51:06 2016

@author: Administrator
"""

class Ball:
    def __init__ (self, color, size, direction) :
        self.color = color
        self.size = size
        self.direction = direction
    def f(self):
        print "내 색은 ", self.color ,  "내 크기는 " , self.size, "내 방향은 ", self.direction ,"이다"

BallA = Ball("red", "small", "down")
BallB = Ball("blue", "big", "up")
BallA.f()
BallB.f()
Ball.f(BallA)