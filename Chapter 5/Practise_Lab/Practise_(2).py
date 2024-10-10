##validating a user input that this value 

##predifined vowels
vowels = ("a","e","i","o","u")

##function to validate character is vowel or not
def validation(value):
    try:
        if len(value) <=1 and value in vowels:
            print(f"Your value {value} is in vowels list")
        else:
            if len(value) >1:
                print("As we already informed you that char should not be more then 1")
            elif value not in vowels:
                print("Your value is not in the list")
            else:
                print("You have passed some thing wrong or suspicious")
    except:
        print("You have passed some thing wrong we dont know what")
        return None
    

##taking a input from the user
user_input = input("Enter your character check whether it is vowel or not = ")


##Calling validation function and passing value in it
result = validation(user_input)


