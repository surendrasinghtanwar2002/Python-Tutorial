"Welcom to our dictionary where we will use dictionary method and form a custom input dictionary application"
#heading of the dictionary
heading= "*** Welcome to Your Dictionary ***"
print(heading.center(180))

#In this we will create our own dictionary with demo details
my_dictionary={
    "User_Name": "Demo",
    "User_LastName": "Demo",
    "User_Contact_no":123456798,
    "User_Exist": False
}
#Dictionary Menu with choice option
secondheading = "Please choose your prefernce from below list ->"
print(secondheading.center(50))
print("\n(1) Display the Dictionary:")
print("\n(2) Add items:")
print("\n(3) Remove Items:")
print("\n(4) Get Items:")
print("\n(5) Remove Dictionary:")

thirdchoice = int(input("\nEnter Your Choice from (1-5): ").center(40))

#Match Case Statement implementing in the dictionary to make menu working
match thirdchoice:
    case 1:
        print("You have choosen first option")
    
    case 2:
        print("You have choosen second option")

    case 3:
        print("You have choosen third option")
    
    case 4:
        print("You have choosen Fourth option")

    case 5:
        print("You have choosen Fifth option")
    
    case _:
        print("You have given wrong input please give right option")
    