# Creating a Grade Calculator using python
str = """ ""Welcome to Grade Calculator"" """
x = str.center(140)
print(x)
A = 100
B = 90
C = 80
D = 70
E = 60
y = int(input("Enter your Total no = "))
if (y>=B and y<=A):
    print("Your grade is A")
elif (y>=C and y<=B):
    print("Your grade is B")
elif (y>=D and y<=C):
    print("Your grade is C")
elif(y>=E and y<=D ):
    print("Your grade is D")
else:
    print("You are fail")

