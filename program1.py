# input 
num1 = eval(input("Enter the first number...")) 
num2 = eval(input("Enter the 2nd number...")) 
  
if(num1 > num2):
    print(num1," is largest no")
elif(num2 > num1):
    print(num2," is largest no")
else:
    print(num1, num2,"both are equal")