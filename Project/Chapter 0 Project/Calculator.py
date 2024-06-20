#In this section we will create a calculator using python using input function & some basic assignment operators and include some basic escape character also.
print("\t\t\t\t\t\t\t\t\t Welcome to All in one \"Calculator\"")
print("Github: surendrasinghtanwar2002 \t\t\t\t\t     \"Origin by 98 Down Street\" \t\t\t\t\t\tLinkedin:surendrasinghtanwar")
Firstno = input("Enter your First no: ")
Secondno = input("Enter your Second no: ")
Choice = input("Enter your operator you need to perform \"+,-,/,*,%,//,**\": ")
if Choice == "+":
    print("Your addition of two number is=",int(Firstno)+int(Secondno))
elif Choice == "-":
    print("Your subtraction of two number is", int(Firstno)-int(Secondno))
elif Choice == "*":
    print("Multiplication of two number is", int(Firstno)*int(Secondno))
elif Choice == "%":
    print("Reminder of two number is",int(Firstno)%int(Secondno))
elif Choice == "//":
    print("Floor division of two number is", int(Firstno)//int(Secondno))
elif Choice == "**":
    print("Exponential operator of two number is", int(Firstno)**int(Secondno))
else:
    print("\"Please choose the correct option you have not choosen the valid option\"")