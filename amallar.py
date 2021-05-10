# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:59:57 2021

@author: FM
"""

print("\nDasturdan chiqish uchun exit buyrug'ini kiriting!\n")

while True:
    son = input("Birinchi sonni kiriting: ")
    son2 = input("Ikkinchi sonni kiriting: ")
    amal = input("Amalni kiriting: ")
    if son == 'exit' or son2 == 'exit' or amal == 'exit':
        break
    ison = float(son)
    ison2 = float(son2)
    if amal=="+":
        print(f"{ison} + {ison2} = {ison+ison2}")
    elif amal=="-":
        print(f"{ison} - {ison2} = {ison-ison2}")
        
    elif amal=="/":
        print(f"{ison} / {ison2} = {ison/ison2}")
    elif amal=="*":
        print(f"{ison} * {ison2} = {ison*ison2}")
    else:
        break