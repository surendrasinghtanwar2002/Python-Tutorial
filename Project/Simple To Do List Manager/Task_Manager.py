                                                                                                ## Library Management System ##
##Importing modules
import os
from time import sleep


##predefined list for the book
library_books = {"Code with C++": "2 Pieces"},{"C++":"Harish Kumar"},{"Oops With Java":"Jameson"}

## Add Book Menu through the list:
Add_Book_Menu = ["Add a Book", "View Books", "Remove Books","Exit"]

##user details predefined
user_details_list = {"admin": "admin@123","user":"user@123","user2":"user@!23"}

##welcome message function
def welcomefunction():
    sleep(2)                     
    os.system('clear')   
    welcome_message = " Library Management System ".center(125,"*")
    print(welcome_message)
    return welcome_message

##Taking user credentaisl for login
def existing_user ():
    create_login = str(input("Enter your username: "))
    create_password = str(input("Enter your password: "))
    if create_login in user_details_list and user_details_list[create_login] == create_password:
        print("Access Granted")
        return True
    elif create_login and create_password not in user_details_list:
        print("Your data is not in our database:")
        if create_login and create_password not in user_details_list:
            join_login= input("Enter your New username: ")
            join_password = input("Enter your New password: ")
            user_details_list.update(join_login,join_password)
            sleep(2)
            print("Your data have been updated")
        else:
            print("Your data have not been updated due to some technical issue")
            return False


result = existing_user()
 ##  Main Menu Looping through the list##
if result != None:
    sleep(2)
    os.system("clear")
    welcomefunction() ##calling a welcome function here
    main_menu = ["Add a new Book","View all books","Borrow a book","Return a book","Exit"]
    for index_menu, menu_list in enumerate(main_menu, start= 1):
        print(index_menu, menu_list)
    while True:
        user_input = int(input("Enter your choice from the above list: "))
    ##Main screen option from the list
        if user_input == 1:
            user_add_choice = input("Press \"Y\" to continue and \"N\" to exit: ")
        ##Add Book menu scree start -------------------->
        if user_add_choice == "Y" or "y":
            sleep(1)
            os.system("clear")
            for index,bookmenu in enumerate(Add_Book_Menu,start=1):
                print(index,bookmenu)
            addbookmenu = int(input("\n Enter your choice from the above list: "))
            ##Add book menu first option start --------------------->
            if addbookmenu == 1:
                sleep(2)
                os.system("clear")
                welcome_message1 = " Library Add Book Section "
                print(welcome_message1.center(125,"*"))
                i=0
                user_book_length = int(input("Enter number of book you have to add (Max 5): ") or 5) 
                while i < user_book_length:
                    book__name = input("Enter your book name = ")
                    book_author_name = input("Enter your book author name: ")
                    if book__name and book_author_name not in library_books:
                        library_books.append({book__name,book_author_name})
                        sleep(2)
                        print("Your book have been added to our database")
                        sleep(1)
                        os.system("clear")
                    elif  book__name and book_author_name in library_books:
                            print("Please Choose correct option: ")
                    else:
                        pass
                    i+=1
                break
            ##Add Book menu first option end !!!!!!!!!!!!!!!!!!!!

            ##Add Book menu second option start ----------------------->
            elif addbookmenu == 2:
                os.system('clear')
                sleep(1)
                for book_sequence,book_names in enumerate(library_books,start=1):                           ##working here
                   print(book_sequence, book_names)
                break
            ##Add Book menu second option end --------------------------->

            ##Add Book menu third option start ------------------------>
            elif addbookmenu == 3:
                print("We will remove the book after some circumstances")

            ##Add Book menu second option end ------------------------->
            elif addbookmenu == 4:
                user_exit_choice = input("Please Press \"Q\" for Quit and \"N\" for cancel this task")
                if user_exit_choice == "q" or "Q":
                    pass
                break
        else:
            print("We are putting you back to our main menu list = ")
            sleep(2)
            os.system('clear')
            end_message = " Thank you Visit Again "
            print(end_message.center(125,"*"))
        ##Loop over 
else:
    print("Can't proceed without the proper user credentials")

##While Loop





