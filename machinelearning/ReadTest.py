# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:38:26 2015

@author: Administrator
"""
import cPickle
import matplotlib.cm as cm
import matplotlib.pyplot as plt

filename = "test.pkl"

# pkl file open
f = open(filename, "rb")

# train_set, valid_set, test_set 
train_set, valid_set, test_set = cPickle.load(f)

# divide imagefile, answer 
imagefile, answer = train_set

# image print
plt.imshow(imagefile[0].reshape((100,100)), cmap=cm.Greys_r)

# show answer 
print answer[0]

# show plot
plt.show()
