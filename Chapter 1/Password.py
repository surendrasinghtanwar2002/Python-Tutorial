#Simple Password Validator using various string methods
import re
Minimum_Length_Password = 6
Maximum_Length_Password = 12
Passwordregex = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
Name = input("Enter your Name = ")
Password = input("Enter your Password Please = ")
result = re.search(Passwordregex,Password)
if (str(Password) <= str(Minimum_Length_Password) and Password.isalpha() and Password.isdigit()):
    print("Your Password length is too low and contains only character you can't proceed with such low password")
elif (Password == Name):
    print("You can't take a name as a password because it might be risky")
elif (result):
    print("Your password is right you can proceed")
else:
    print("You should practise or generate password from best password generator tool")