# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 21:24:25 2022

@author: Admin
"""

import random

name = ['John', 'Tom', 'Alex', 'Audrey', 'Jeff']
verb = ['kicks', 'punches', 'hugs', 'likes', 'hits']
noun = ['apples', 'pillows', 'bananas', 'people', 'laptops']

print(name[random.randrange(0,len(name))],verb[random.randrange(0,len(verb))],noun[random.randrange(0,len(noun))])

