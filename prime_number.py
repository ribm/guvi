# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:07:55 2019

@author: kr151
"""
"""
Finding the all prime number given input as a list of numbers.
"""
input_list_length = int(input("Enter the length"))
input_list = []
prime_list =[]
for number in range(input_list_length):
    input_i = int(input("Enter the number"))
    input_list.append(input_i)
print(input_list)    
for num in input_list:
    if num > 1:
        for i in range(2,(num)):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
        else:
             print(num,"is a prime number")
             prime_list.append(num)
             
    else:
         print(num,"is not a prime number")

print(prime_list)            
    