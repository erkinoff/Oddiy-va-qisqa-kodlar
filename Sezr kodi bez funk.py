# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 20:19:07 2021

@author: FM
"""

'''Sezar kodi'''
a = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzz_"
son = int(input("Shifrlash raqamini kiriting: "))
soz = input("Shifrlanadigan matnni kiriting: ")
for i in soz:
    if i in a:
        joyi = a.find(i)
        if i == "_" or i == "'":
            print(i, end = '')
        else:
            print(a[joyi+son], end = '')