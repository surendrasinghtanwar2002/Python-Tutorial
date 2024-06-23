# Write a program that takes two integers as input from the user and checks whether the first number is a multiple of the second number.
#If it is, print "The first number is a multiple of the second number." Otherwise, print "The first number is not a multiple of the second number."

first_no = int(input("Enter your first no"))
second_no = int(input("Enter your second no"))
if (first_no%second_no !=0):
    print("Your first no is not multiple of second no")
else:
    print("Your first no is multiple of second no")