# Question 2:
# Write a program that takes an integer input from the user and checks whether the number is divisible by 5.
#If it is divisible by 5, print "The number is divisible by 5." Otherwise, print "The number is not divisible by 5."
A = int(input("Enter your first no = "))
if( A%5 !=0):
    print("Your no is not divisible by 5")
else:
    print("Your no" ,A, "is divisible by 5")