# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:07:57 2015

@author: Administrator
"""

import PIL
from PIL import Image

# image resize use
hsize = 100
basewidth = 100

# image open
img = Image.open('Tulips.jpg')

# image convert
r, g, b = img.split()
img = Image.merge("RGB", (r, g, b))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

# black & white convert
img = img.convert('L')

# save image
img.save('0_modified.jpg')
print('완료')
