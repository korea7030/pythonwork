# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 20:54:14 2015

@author: Administrator
"""
list_year = []
list_brand = []
list_probarea = []


def make_optionlist():
    for i in range(1, 4):
        filename = 'listoption' + str(i) + '.txt'
        f = open(filename, 'r')

        # print(filename)
        for line in f.readlines():
            if (filename == 'listoption1.txt'):
                list_year.append(line.strip())
            elif (filename == 'listoption2.txt'):
                list_brand.append(line.strip())
            else:
                list_probarea.append(line.strip())


if __name__ == '__main__':
    make_optionlist()

    # print(str(list_year))
    # print(str(list_brand))
    # print(str(list_probarea))
