# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 19:58:19 2022

@author: Admin
"""
highest = 0
lowest = 0
x = []
for i in range(3):
    y = int(input('Insert Score: '))
    x.append(y)
    
print(x)

#94, 87, 100


if x[0] > x[1] and x[0] > x[2]:
    highest = x[0]
elif x[1] > x[0] and x[1] > x[2]:
    highest = x[1]
elif x[2] > x[0] and x[2] > x[1]:
    highest = x[2]
elif x[0] < x[1] and x[0] < x[2]:
    lowest = x[0]
elif x[1] < x[0] and x[1] < x[2]:
    lowest = x[1]
else:
    lowest = x[2]
    
print("Highest: ", highest)
print("Lowest:", lowest)