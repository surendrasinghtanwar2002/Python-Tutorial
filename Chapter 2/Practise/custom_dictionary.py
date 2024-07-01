"Welcom to our dictionary where we will use dictionary method and form a custom input dictionary application"
#heading of the dictionary
heading= "*** Welcome to Your Dictionary ***"
print(heading.center(180))

#In this we will create our own dictionary with demo details
my_dictionary={
 "name": "Radhe",
 "course": "Bca",
 "Class": "Radhe",
 "Contact_no": "Bca"
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
        print(thirdchoice,"option selected")
        if (len(my_dictionary)==0):
            print(("!!! Your dictionary is empty !!!").center(80))
        else:
            print(my_dictionary.items())

    case 2:
        print(thirdchoice,"\noption selected")
        adding_item=int(input("\nEnter the items values to add in the dictionary: "))
        for i in range(adding_item):
            key= (input("Enter your key name: "))
            value = (input("Enter your value: "))
            my_dictionary[key]=value
        print("Your updated dictionary is", my_dictionary.values())

    case 3:
        print(thirdchoice,"\noption selected")
        removing_item= int(input("Enter the items value to remove from the dictionary"))
        for i in range(removing_item):
             
            
    case 4:
        print("You have choosen Fourth option")

    case 5:
        print("You have choosen Fifth option")
    
    case _:
        print("You have given wrong input please give right option")
    