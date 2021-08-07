# CALCULATOR

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

    

p=input("select the operator \n"
         "1. Addition\n"
         "2. Substration\n"
         "3. Division\n"
         "4. Multiplication\n"
         )
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))

if p=="1":
    add(a,b)
elif p=="4":
    multiply(a,b)
elif p=="2":
    sub(a,b)
elif p=="3":
    divide(a,b) 

else: print("invalid") 

