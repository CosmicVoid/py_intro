# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 18:43:11 2022

@author: Admin
"""

x = [['a',100],['b',95],['c',88]]
'print(x[1][0])'


letter = [x[i][0] for i in range(len(x))]
num = [x[i][1] for i in range(len(x))]
max_x = num.index(max(num))
print(f'Highest: {letter[max_x]}, {max(num)}')
min_x = num.index(min(num))
print(f'Lowest: {letter[min_x]}, {min(num)}')