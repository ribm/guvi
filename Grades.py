# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 08:59:38 2019

@author: kr151
"""

subject1 = int(input("Enter the makrks for sub1...."))
subject2 = int(input("Enter the makrks for sub2...."))
subject3 = int(input("Enter the makrks for sub3...."))
subject4 = int(input("Enter the makrks for sub4...."))
subject5 = int(input("Enter the makrks for sub5...."))


Average_Marks = (subject1 + subject2 +subject3 +subject4 + subject5)//5
print(Average_Marks)
if (Average_Marks > 90):
    print("Grade A+")
if (Average_Marks > 80 and Average_Marks <= 90):
    print("Grade A")
elif (Average_Marks > 70 and Average_Marks <= 80):
    print("Grade B")
elif (Average_Marks > 60 and Average_Marks <= 70):
    print("Grade C")
elif (Average_Marks > 50 and Average_Marks <= 60):
    print("Grade D")
else:
    print("Grade E")