#Practising variable and datatypes
a = 152525252225
print(a)

#Printing basic variables using print command
b= "Surendra Singh Tanwar"
c = 919191919
d= 25.602500
e = True
f = None
print(b)

#Priting both values a & b using + operator tgere is a mistory that when we try to merger different datatypes using + operator then it will show error (TypeError: unsupported operand type(s) for +: 'int' and 'str' )
#Because + operator is being used to print the same datatype at a same time 
# So for solving that either we use , comma to instruct python  that they both are different datatypes or either
# convert one datatype to first operand to print both value in print
print(a+c)

#for printing two different datatypes i am using a str() method to convert numerical value to string because
#my first operand is string
print(b+str(a)+str(c))

#for finding any variable datatype so we will use the type() method or function

print("So type of a is",type(a))
print("So type of b is",type(b))
print("So type of c is",type(c))
print("So type of d is",type(d))
print("So type of e is",type(e))
print("So type of f is",type(f))

#for finding any variable and using + operator with the type() method or function then
# we have to do something crazy because without doing this it will show the error because type will also not print the string
#output
#so for using + operator with type function we need to conver the output of type function to string 
print("The datatype of a is"+ str(type(a)))
print("The datatype of b is"+ str(type(b)))
print("The datatype of c is"+ str(type(c)))
print("The datatype of d is"+ str(type(d)))
print("The datatype of e is"+ str(type(e)))
