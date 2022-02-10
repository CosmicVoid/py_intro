# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 18:44:48 2022

@author: Admin


x = {}
x['num'] = 10
print(2 in x)
"""

data = {'A001':['Gummy Bear',20],'A002':['Popsicle',25],'A004':['Instant Noodle',10],'A006':['Soda',30]}

while True:
    ans = int(input("1.Search Item\n2.Close System\nInsert: "))
    if ans==1:
        num = input('Insert Item ID: ')
        if num not in data:
            print('ID: {} Does not exist'.format(num))
            new=input('Do you want to add this item?(Y or N) ')
            if new=='Y':
                name=int(input("Insert Item Name: "))
                price=int(input("Insert Item Cost: "))
                data[num]=[name, price]
                d=data.get(num)
                print('ID:{} Name:{} Price:${}'.format(num,d[0],d[1]))
        else:
            print("ID:{} Price:${}".format(data[num][1],data[num][1]))
    elif ans==2:
        break
    else:
        print("Invalid Command, Please Try Again")