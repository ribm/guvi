# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 09:28:40 2019

@author: kr151
"""

Eunit = int(input("Enter the E unit...."))

Amount = 0


if (Eunit  < 90):
    print(45*Eunit)
elif (Eunit  < 80):
    print(40*Eunit)
elif (Eunit  < 70):
    print(35*Eunit)
elif (Eunit  < 60):
    print(30*Eunit)
else:
    print(0)
    
