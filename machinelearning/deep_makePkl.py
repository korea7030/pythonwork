# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:33:52 2015

@author: Administrator
"""

import cPickle
import PIL
from PIL import Image
import numpy

hsize = 100

# read maked image file
I = numpy.asarray(PIL.Image.open('0_modified.jpg'))

# pixel list
arr = []

# to make pkl file
# 0~255 normalization
for i in range(0, len(I) * hsize):
    arr.append(numpy.float32((I[i / hsize][i % hsize] / 255.0)))

# numpy.array type convert
arr = numpy.array(arr)

# .pkl format
imagearr = [arr]
imagearr = numpy.array(imagearr)

# answer = 1 hard coding
answer = 1
answerarr = [answer]
answerarr = numpy.array(answerarr)

train_set = (imagearr, answerarr)
valid_set = (imagearr, answerarr)
test_set = (imagearr, answerarr)

data_set_list = [train_set, valid_set, test_set]

# make pkl
f = open("test.pkl", "wb")
f.write(cPickle.dumps(data_set_list))
