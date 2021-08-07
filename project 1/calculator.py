# CALCULATOR
import math
def add(a,b):
    result=a+b
    print(result)

def multiply(a,b):
    result=a*b
    print(result)

def sub(a,b):
    result=a-b
    print(result)   

def divide(a,b):
    result=a/b
    print(result) 

def square(a):
        result=str(int(a*a))
        print(result)

def root(a):
    root= math.sqrt(a)
    result=str(float(root))    
    print(result)    

p=input( "1. Addition\n"
         "2. Substration\n"
         "3. Division\n"
         "4. Multiplication\n"
         "5. square\n"
         "6. root\n"
         "Choose an operation to perform \n"
         )

if p=="1":
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:")) 
    add(a,b)
elif p=="4":
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:")) 
    multiply(a,b)
elif p=="2":
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:")) 
    sub(a,b)
elif p=="3":
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:")) 
    divide(a,b) 
    
elif p=="5":
    a =int(input("enter the number"))
    square(a)

elif p=="6":
    a =float(input("enter the number"))
    root(a)

else: print("invalid") 

