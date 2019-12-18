# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:29:12 2019

@author: kr151
"""

        
amount = int(input("Enter the amount:-"))        
        
notes = [2000, 500, 200, 100, 
               50, 20, 10, 5, 1] 
                 
noteCounter = [0, 0, 0, 0, 0, 
                     0, 0, 0, 0] 
      
print ("Currency Count -> ") 
      
for i, j in zip(notes, noteCounter):
    
    if amount >= i:
        
        j = amount // i 
        amount = amount - j * i 
        print (i ," : ", j)
        


    
    
    
    

