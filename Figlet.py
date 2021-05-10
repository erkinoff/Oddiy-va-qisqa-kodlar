# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:11:08 2021

@author: FM
"""

from pyfiglet import Figlet
text = Figlet(font = "doh", direction = 'auto', justify = 'auto', width = 140)
print(text.renderText("salom"))
