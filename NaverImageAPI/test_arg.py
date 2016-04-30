# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 18:42:51 2016

@author: Administrator
"""

import sys
 
# Get the total number of args passed to the demo.py
total = len(sys.argv)
 
# Get the arguments list 
cmdargs = str(sys.argv)

# Print it
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)