# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 19:50:38 2015

@author: Administrator
"""

import pandas as pd
import numpy as np
import os
from collections import Counter 

os.getcwd()

df = pd.read_json("train.json")

df.head()

## cuisine  Distribution
cuisine_Distribution = Counter(df.cuisine)
cuisine_Distribution

cuisine_fig = pd.DataFrame(cuisine_Distribution, index=[0]).transpose()[0].sort(ascending=False, inplace=False).plot(kind='barh')
cuisine_fig.invert_yaxis()
cuisine_fig = cuisine_fig.get_figure()
cuisine_fig.tight_layout()
cuisine_fig.savefig("Cuisine_Distribution.jpg")

## Recipe Distribution
recipe_Distribution = [Counter(recipe) for recipe in df.ingredients]
recipe_Distribution

ingredient_Distribution = sum(recipe_Distribution, Counter())
ingredient_fig = pd.DataFrame(ingredient_Distribution, index=[0]).transpose()[0].sort(ascending=False, inplace=False)[:30].plot(kind='barh')
ingredient_fig.invert_yaxis()
ingredient_fig = ingredient_fig.get_figure()
ingredient_fig.tight_layout()
ingredient_fig.savefig("Ingredient_Distribution.jpg")