num1=float(input("enter the 1st num:"))
num2=float(input("enter the 2nd num:"))
num3=float(input("enter the 3rd num:"))
if(num1>=num2)and(num1>=num3):
   largest=num1
elif(num2>=num1)and(num2>=num3):
    largest=num2
else:
    largest=num3
print("the largest number is",largest)
