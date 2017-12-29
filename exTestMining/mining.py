# -*- coding: utf-8 -*-

"""
Created on Mon Sep 28 12:13:15 2015

@author: Administrator
"""

import nltk
import pip


nltk.download('gutenberg')
nltk.download('maxent_treebank_pos_tagger')

from nltk.corpus import gutenberg

files_en =  gutenberg.fileids()
doc_en =gutenberg.open('austen-emma.txt').read()

from nltk import regexp_tokenize
pattern= r'''(?x) ([A-Z]\.)+ | \w+(-\w+)* | \$?\d+(\.\d+)?%? | \.\.\. | [][.,;"'?():-_`]'''
tokens_en = regexp_tokenize(doc_en, pattern)

en = nltk.Text(tokens_en)

print(len(en.tokens))
print(len(set(en.tokens)))
en.vocab()

en.plot(50)

from matplotlib import pylab
pylab.show = lambda: pylab.savefig('some_filename.png')
pylab.show

## dispersion_plot
en.dispersion_plot(['Emma', 'Frank', 'Jane'])

## concordance
en.concordance('Emma', lines=5)

en.similar('Emma')
en.similar('Frank')

tokens = "The little yellow dog barked at the Persian cat".split()
tags_en = nltk.pos_tag(tokens)

tags_en

parser_en = nltk.RegexpParser("NP : {<DT>?<JJ>?<NN.*>*}")
chunks_en = parser_en.parse(tags_en)
chunks_en.draw()

## Preprocessing
from nltk.corpus import reuters 

