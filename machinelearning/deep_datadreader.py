# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 18:32:44 2015

@author: Administrator
"""

import cPickle
import matplotlib.cm as cm
import matplotlib.pyplot as plt

filename = "mnist.pkl"

f = open(filename, "rb")

train_set, valid_set, test_set = cPickle.load(f)

print("train_set[0][0] : " + str(train_set[0][0]))

print("train_set[1][0] : " + str(train_set[1][0]))

print("train_set[0][0] 길이 : " + str(len(train_set[0][0])))

print("train_set[0] 길이 : " + str(len(train_set[0])))

print("train_set[1]의 길이 : " + str(len(train_set[1])))

imagefile, answer = train_set

print(train_set)
print(valid_set)
print(test_set)

type(train_set)
plt.imshow(imagefile[0].reshape((28, 28)), cmap=cm.Greys_r)

print answer[0]

plt.show()
