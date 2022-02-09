# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:22:11 2022

@author: Admin
"""
while 1==1:
    command = int(input("What is the command? "))
    if command==1:
        amount = int(input("What is the initial amount of apples: "))
        cost = int(input("What is the cost of each apple: "))
    elif command==2:
        stock = int(input("How many apples were stocked: "))
    elif command==3:
        sells = int(input("How many apples were sold: "))
    elif command==4:
        print("You earned $",cost*sells)
    elif command==5:
        print("You have", amount+stock-sells, "apples left")
    elif command==6:
        break
    else:
        print("This is not a command, please choose 1 to 6")