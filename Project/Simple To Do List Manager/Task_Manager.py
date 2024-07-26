                                            ##Library Management System
##Importing modules
import os
from time import sleep

##Banner of the Library Management System
sleep(2)                        ##Sleep function
os.system('clear')              ## It will clear previous data from the console
welcome_message = " Library Management System "
print(welcome_message.center(125,"*"))

## USER MENU Looping through the list##
user_menu = ["Add a new Book","View all books","Borrow a book","Return a book","Exit"]
for index_menu, menu_list in enumerate(user_menu, start= 1):
    print(index_menu, menu_list,":")
        

##While Loop
while True:
    user_input = int(input("Enter your choice from the above list: "))
    if user_input == 1:
        print("You want a new book1")
    elif user_input == 2:
        print("You want to view all the book")
    elif user_input == 3:
        print("You want to Borrow a book")
    elif user_input == 4:
        print("You want to return a book")
    else:
        user_exit_choice = (input("You want to exit \"Q\" for quit and \"N\" for return to the menu = "))
        if user_exit_choice == "q" or "Q":
            pass
        break

##Loop over
sleep(2)
os.system('clear')
end_message = " Thank you Visit Again "
print(end_message.center(125,"*"))


