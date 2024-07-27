                                            ##Library Management System
##Importing modules
import os
from time import sleep

##Banner of the Library Management System
sleep(2)                        ##Sleep function
os.system('clear')              ## It will clear previous data from the console
welcome_message = " Library Management System "
print(welcome_message.center(125,"*"))


##predefined list for the book
library_books = [{"Code with C++": "2 Pieces"}]

##  Main Menu Looping through the list##
main_menu = ["Add a new Book","View all books","Borrow a book","Return a book","Exit"]
for index_menu, menu_list in enumerate(main_menu, start= 1):
    print(index_menu, menu_list,":")  

## Add Book Menu through the list:
Add_Book_Menu = ["Add a Book", "View Books", "Remove Books","Exit"]


##While Loop
while True:
    user_input = int(input("Enter your choice from the above list: "))
    ##choice 1 from the list
    if user_input == 1:
        user_add_choice = input("Press \"Y\" to continue and \"N\" to exit: ")
        if user_add_choice == "Y" or "y":
            sleep(1)
            os.system("clear")
            for index,bookmenu in enumerate(Add_Book_Menu,start=1):
                print(index,bookmenu)
            addbookmenu = int(input("\n Enter your choice from the above list: "))
            if addbookmenu == 1:
                sleep(2)
                os.system("clear")
                i=0
                user_book_length = int(input("Enter number of book you have to add (Max 5): ") or 5) 
                while i < user_book_length:
                    book__name = input("Enter your book name = ")
                    book_author_name = input("Enter your book author name: ")
                    if user_input and book_author_name not in library_books:
                        library_books.append({book__name,book_author_name})
                        sleep(2)
                        print("Your book have been added to our database")
                        sleep(1)
                        os.system("clear")
                    i+=1
                    
                   
            elif addbookmenu == 2:
                print("We will start this service soon")
            elif addbookmenu == 3:
                print("We will remove the book after some circumstances")
            elif addbookmenu == 4:
                user_exit_choice = input("Please Press \"Q\" for Quit and \"N\" for cancel this task")
                if user_exit_choice == "q" or "Q":
                    pass
                break
        else:
            print("We are putting you back to our main menu list = ")
            sleep(1)
            break
    ## choice 2 from the list
    elif user_input == 2:
        print("You want to view all the book")
    ## choice 3 from the list
    elif user_input == 3:
        print("You want to Borrow a book")
    ## choice 4 from the list
    elif user_input == 4:
        print("You want to return a book")
    ##choice 5 from the list
    elif user_input == 5:
        user_exit_choice = (input("You want to exit \"Q\" for quit and \"N\" for return to the menu = "))
        if user_exit_choice == "q" or "Q":
            pass
        break

##Loop over
sleep(2)
os.system('clear')
end_message = " Thank you Visit Again "
print(end_message.center(125,"*"))


