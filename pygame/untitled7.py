# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 11:57:05 2016

@author: Administrator
"""

import cPickle as pickle

my_list = ['Fred', 73, 'Hello there', 81.9876e-13]
pickle_file = open('my_pickled_list.pkl', 'wb')
pickle.dump(my_list, pickle_file)

pickle_file = open('my_pickled_list.pkl', 'rb')
recovered_list = pickle.load(pickle_file)
pickle_file.close()

print recovered_list