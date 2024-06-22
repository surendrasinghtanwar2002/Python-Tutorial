#Find pythagorean is valid or not 
FirstNo = int(input("Enter your First Leg no = "))
SecondNo = int(input("Enter your Second Leg no = "))
ThirdNo = int(input("Enter your Hypotenuse no = "))
if (FirstNo**2 + SecondNo**2 == ThirdNo**2):
    print("1")
else:
    print("0")