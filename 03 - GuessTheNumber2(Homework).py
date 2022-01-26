# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 20:18:36 2022

@author: Admin
"""

import random
r = random.randint(1,20)
i = 5
while i>0:
    guess = int(input("Guess a number from 1 to 20: "))
    if r == guess:
        print("You are correct!")
        break
    elif i <= 1:
        print("Sorry, You have no lives left")
        break
    else:
        i = i - 1
        print("You are incorrect("+str(i)+" lives left)")