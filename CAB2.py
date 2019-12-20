# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:10:11 2019

@author: kr151
"""
import sys
from random import randint
Source = ["A","B","C","D","E","F","G","H","I"]
Destination = ["A","B","C","D","E","F","G","H","I"]
Username = ["GUVI","A","B","C","D","E","F","G","H","I"]
Password = ["GUVI","A","B","C","D","E","F","G","H","I"]
Category = ["Mini", "Sedan", "Premium"]
Cat_dict = {"Mini":["swift", "indica"],"Sedan":["cruze", "punto"],"Preminum":["benz", "audi"]}
cost_per_km = {"Mini":5,"Sedan":7,"Preminum":10}
dist_dict ={}

for s in Source:
    for d in Destination:
        dist_dict[s+d]=randint(0, 100)


def del_fromlist(value,list_name):
    list_name.remove(value)
    print("value removed")
def auth():
    E_Username = input("Please Enter the username....")
    Pass = input("Please Enter the password....")
            
    count =0
    while count<3:
           
       
        
    
        if E_Username not in  Username or Pass not in Password:
            print("please enter valid Usename or pass ...note:- max try- 3 times....")
            E_Username = input("Please Enter the username....")
            Pass = input("Please Enter the password....")
            count+=1
            if count==3:
                  print("exiting the App")
                  sys.exit()
            
        else:
            return 1
        
            
def location_entry():
    
    Source1 = input("Please Enter the Source....")
    count =0
    while count<2:
           
           if Source1 not in Source:
               print("please enter valid Source ...note:- max try- 3 times....")
               Source1 = input("Please Enter the valid Source....")
               
               count+=1
               print(count)
               if count==2:
                  print("exiting the App")
                  sys.exit()
           else:
               break
    count =0        
    while count<2:
          Destination1 = input("Please Enter the Destination....")
          if Destination1 not in Destination:
              print("please enter valid Destination ...note:- max try- 3 times....")
              Destination1 = input("Please Enter the Destination....")
              count+=1
              if count==2:
                  print("exiting the App")
                  sys.exit()
              
          else:
              break
    count =0
    while count<2:
          category = input("Please Enter the category....")
          if category not in Category:
              print("please enter valid category ...note:- max try- 3 times....")
              category = input("Please Enter the category....")
              count+=1
              if count==2:
                  print(" EITHER CAB alredy in use or wrong password exiting the App")
                  sys.exit()
          else:
              del_fromlist(category, Category)
              return Source1, Destination1, category
    
              
def reciept(values):
    calculated_cost = dist_dict.get(values[0]+values[1])*cost_per_km.get(values[2])
    print("your estimated reciept is:----------------")
    print(values[0],"Your source")
    print(values[1],"Your Destination")
    print(cost_per_km.get(values[2]), "Cost per km")
    print(dist_dict.get(values[0]+values[1]), "Distance")
    print(calculated_cost,"Final Cost") 
    
auth()
x=location_entry()
auth()
y=location_entry()
reciept(x)
    