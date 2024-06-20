#Typecasting in Python, also known as type conversion, is the process of converting one data type into another. 
# This can be done using various built-in functions. There are two types of typecasting: implicit and explicit.

#Implicit Typecasting
#Python automatically converts one data type to another. 
#This happens when performing operations that mix different types, such as integers and floats.
a= 25   #int
b = 35.2 #float
print(a+b)

#Explict Typecasting 
#Explicit typecasting is done manually by the programmer using built-in functions. 
# Common functions for explicit typecasting include int(), float(), str(), and bool().
c = "Surendra" #string
d = 25         #numerical value
#if we use + operator between this two variable it will give error for solving that issue
# we need to convert one data type with string so we will convert d with string value
print(c+str(d))
print(type(c))