# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:22:11 2022

@author: Admin
"""
def options():
    print('\n')
    print("Options:")
    print("(1)Input Price and Initial amount")
    print("(2)Input apples gained")
    print("(3)Input apples sold")
    print("(4)Total Earnings")
    print("(5Total Apples")
    print("(6)Exit")
amount = 0
stock = 0
sell = 0
sells = []
print("vvvvvvvvvvvvvvvvvvvvvv")
print("Apple Recording System")
print("^^^^^^^^^^^^^^^^^^^^^^")

while 1==1:
    options()
    command = int(input("What is the command? "))
    if command==1:
        amount = int(input("What is the initial amount of apples: "))
        print("There are ",amount,"apple(s)")
        cost = int(input("What is the cost of each apple: "))
        print("Apples are now $",cost)
    elif command==2:
        stock = int(input("How many apples have came in: "))
        print(stock,"apples have came in")
        print("You have", amount+stock-sells, "apples")
    elif command==3:
        out = int(input("How many apples were sold: "))
        print("You should charge $",out*cost)
        sell = sell+out
        sells.append(input(out))
        print("You have", amount+stock-sells, "apples")
        print("How many apples each customer bought so far:",sells)
    elif command==4:
        print("You earned $",cost*sells)
        for i in range(len(sells)):
            print(sells[i], 'apples $',sells[i]*cost)
            print("Sold",sell,"apples")
            print("Gained $",sell*cost)
    elif command==5:
        print("You have", amount+stock-sells, "apples")
    elif command==6:
        break
    else:
        print("This is not a command, please choose 1 to 6")