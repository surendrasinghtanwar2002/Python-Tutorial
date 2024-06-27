
#Comparision operator

#First Question Practise Set
a = 5
b = 10
if(a>=b):
    print("A is greater then b")
else:
    print("B is greater then a")

#Second Question Practise Set
number = -2
if (number <0):
    print('Number is negative')
else:
    print("Number is positive")


#Find the largest numbe from three variable
# a = input('Enter your First number')
# b = input("Enter your Second number")
# c = input("Enter your Third number")
# if(a>b):
#     print("a is greater than b & c")
# elif(b>c):
#     print("b is greater than a and c")
# else:
#     print("c is greater than a & b")


#Find even and odd number from the given number
# d = int(input("Enter your number"))
# if (d%2==0):
#     print("d is even number")
# else:
#     print("d is odd number")

# #Leap year find Program
# year = int(input("Enter your year"))
# if (year%4==0 and year%400==0):
#     print("your year is a leap year")
# else:
#     print("your year is not a leap year")

#Grade Classification:
grade = int(input("Enter your Grade = "))
if (grade>=90 and grade<=100):
    print("Your given number",grade,"lies on Grade A")
elif(grade>=80 and grade<=89):
    print("Your given number",grade,"lies on Grade B")
elif(grade>=70 and grade<=79):
    print("Your given number is",grade,"lies on grade C")
elif(grade>=60 and grade<=69):
    print("Your given number",grade,"lies on Grade D")
elif(grade>=45 and grade<=59):
    print("Your given number",grade,"lies on Grade E")
else:
    ("Sorry you have not passed the examination try again next time")