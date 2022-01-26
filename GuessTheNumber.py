# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:09:38 2022

@author: Admin
"""
import random
guess = int(input("Guess a number from 1 to 10: "))
r = random.randint(1,10)
if r == guess:
    print("You are correct!")
else:
    print("You are incorrect, the number is "+str(r))

