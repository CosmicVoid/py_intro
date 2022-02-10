# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 20:01:24 2022

@author: Admin
"""
#There are only 3 words
x={'book':'書','書':'book','banana':'香蕉','香蕉':'banana','apple':'蘋果','蘋果':'apple'} 

print("vvvvvvvvvvvvvvvv\nVocabulary Chart\n^^^^^^^^^^^^^^^^\n")

while True:
    print("1. English to Chinese\n2. Chinese to English\n3. Close")
    command = int(input("What do you need? "))
    if command==1:
        chiToEng = input("What word do you need to translate? ")
        if chiToEng in x:
            print("\nThe translation is {}\n".format(x[chiToEng]))
        else:
            "This word doesn't exist in the chart, please try again"
    elif command==2:
        engToChi = input("What word do you need to translate? ")
        if engToChi in x:
            print("\nThe translation is {}\n".format(x[engToChi]))
        else:
            "This word doesn't exist in the chart, please try again"
    elif command==3:
        print("\nHave a nice day!")
        break
    else:
        print("Invalid Command, Please Try Again")