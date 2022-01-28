# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 19:44:37 2022

@author: Admin
"""

x = []
for i in range(5):
    y = int(input('Insert Score: '))
    x.append(y)
    
print(x)

#94, 87, 100, 78, 97


total = 0
for i in x:
    total=total+i
    
print('Total: ', total)
print('Avg: ', total/5)