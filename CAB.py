# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:32:50 2019

@author: kr151
"""
"""

CAB 
"""

from random import randint
Source = ["A","B","C","D","E","F","G","H","I"]
Destination = ["A","B","C","D","E","F","G","H","I"]
Username = "GUVI"
Password = "GUVI"
Category = ["Mini", "Sedan", "Premium"]
Cat_dict = {"Mini":["swift", "indica"],"Sedan":["cruze", "punto"],"Preminum":["benz", "audi"]}
cost_per_km = {"Mini":5,"Sedan":7,"Preminum":10}
dist_dict ={}
count =0
for s in Source:
    for d in Destination:
        dist_dict[s+d]=randint(0, 100)
print(dist_dict)
        
        
try:
   while count<3:
       
       E_Username = input("Please Enter the username....")
       Pass = input("Please Enter the password....")
    
       if E_Username != Username or Pass != Password:
           print("please enter valid Usename or pass ...note:- max try- 3 times....")
           count+=1
       else:
        break
   if E_Username == Username or Pass == Password :
       
       while count<3:
           Source1 = input("Please Enter the Source....")
           if Source1 not in Source:
               print("please enter valid Source ...note:- max try- 3 times....")
               count+=1
           else:
            break
       while count<3:
          Destination1 = input("Please Enter the Destination....")
          if Destination1 not in Destination:
              print("please enter valid Destination ...note:- max try- 3 times....")
              count+=1
          else:
              break
       while count<3:
          category = input("Please Enter the category....")
          if category not in Category:
              print("please enter valid category ...note:- max try- 3 times....")
              count+=1
          else:
              break
except TypeError:
    print("terminating the session")
    calculated_cost = dist_dict.get(Source1+Destination1)*cost_per_km.get(category)
    print("your estimated reciept is:----------------")
    print(Source1,"Your source")
    print(Destination1,"Your Destination")
    print(cost_per_km.get(category), "Cost per km")
    print(dist_dict.get(Source1+Destination1), "Distance")
    print(calculated_cost,"Final Cost")              
              
       
              

           
           
        
           
         
              

   
       
      
          
        
          
        
    
          
              
            
        
              
         
          
                   
        
              
              
            
        
              
         
          
       
              
         
          

    

            
    
        
    

    
        

        
            

    
    
    

