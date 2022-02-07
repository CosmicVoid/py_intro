# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:57:53 2022

@author: Admin
"""

students = [["Tim",87],["Adrian",92],["Aria",100],["Sia",95]]
name = [students[i][0] for i in range(len(students))]
score = [students[i][1] for i in range(len(students))]
max_num = score.index(max(score))
min_num = score.index(min(score))
print(f'Highest: {name[max_num]}, {max(score)}')
print(f'Lowest: {name[min_num]}, {min(score)}')
avg = 0
for i in score:
    avg = avg+i
avg = avg/len(score)
print(avg)