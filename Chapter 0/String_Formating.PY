#1. How to Format String using % Operator

#using modulus operator we have to specify every datatype with % sign which we perform in c and c++
# %s = for string
# %d = for digit or numerical value
# %f = for floating number

## (1) printing various variable expression using modulus operator (Part 1)
name = "John"
age = 24
college = "Poornima University"
CGPA = 8.59
print("Hello my name is %s and my age is %d and i have completed my bachelors from %s and i have scored %f" %(name,age,college,CGPA))


##(2) printing various variable expression using modulus operator (Part 2)

Full_Name = "Surendra Singh Tanwar"
Age = 24
College = "Poornima University"
Fathers_name = "Vikram Singh Tanwar"
Fathers_occupation = "Teacher"
print("My name is %s and my age is %d and I have completed my bachelors from %s and my father name is %s and my father occupation is %s" %(Full_Name,Age,College,Fathers_name,Fathers_occupation))

##(3) printing various dictionary key expression using modulus operator 
my_dictionary= {
    "Name": "Surendra Singh Tanwar",
    "Age": 29,
    "Subject": "Computer Science",
    "Mobile no": 9460824001,
    "Student": False
}
print("My name is %s and my age is %d and I was a %s student & my contact number is %d and i am not student %d" %(my_dictionary["Name"], my_dictionary["Age"], my_dictionary["Subject"],my_dictionary["Mobile no"],my_dictionary["Student"]))


#2 Format string using Format() method
# In this method we have to only need to specify number along with their value first and then value
# {} in this we will declare no for value and () in this we will declare exact variable or key name.

##(1) Printing various expression of variable using format function (Part 1)
my_name = "Surendra"
my_last_name = "Singh Tanwar"
my_contact_number = 9460824001
print("My name is {0} and my last name is {1} and my contact number is {2}".format(my_name,my_last_name,my_contact_number))

##(2) Printing various expression of variable using format function (Part 2)
my_friend_name = "Sohan"
my_friend_father_name = "Mohan"
my_friend_house_no = "18"
print("Hello my name is Surendra Singh and my friend name is{0} and his father name is{1} and his house no is{2} ".format(my_friend_name,my_friend_father_name,my_friend_house_no))

##(3) Printing various expression of dictionary keys using format function
my_dictionary={
    "Name": "Surendra Singh Tanwar",
    "Fathers_name": "Vikram Singh Tanwar",
    "Mobile no": 9460824001,
    "Designation": "Software Engineer"
}
print("Hello my name is {0} and my father's name is {1} and my contacy number is {2} and currently i am on {3}" .format(my_dictionary["Name"], my_dictionary["Fathers_name"],my_dictionary["Mobile no"],my_dictionary["Designation"]))

#3 Formating string using F-strings methods in python
# Python offers a powerful feature called f-strings (formatted string literals) to simplify string formatting and interpolation. f-strings is introduced in Python 3.6 it provides a concise and intuitive way to embed expressions and variables directly into strings. 
# Interpolation means easy to insert various kind of expression in the existing string
#To create an f-string, prefix the string with the letter “ f ”. The string itself can be formatted in much the same way that you would with str.format().


##(1) Printing various expression using f-string (Part 1)
val = "Geeks"
val2 = "For learners"
val3 = 19
print(f"{val} is being used by developers for learning various kind of programming language and its famous place {val2} from past {val3}")


##(2) Printing various expression using f-string and converting value into float (Part 2)
value_1 = 20
value_2 = 30
value_3 = 50
print(f"{value_1+value_2+value_3: .2f}") #this : .2f method is being used to convert int into float after addition

##(3) Printing various expression of dictionary keys using f-string function
my_first_dictionary = {
    "Name": "Surendra Singh Tanwar",
    "Email-Address": "surendrasinghtanwar667@gmail.com",
    "Mobile_no": 9460824001,
    "Fathers_Name": "Vikram Singh Tanwar"
}
print(f"My name is {my_first_dictionary["Name"]} and my email address is {my_first_dictionary["Email-Address"]} and my mobile no is {my_first_dictionary["Mobile_no"]} and my father name is{my_first_dictionary["Fathers_Name"]}")

##(4) Printing various variable expression using f-string function
English = 70
Hindi = 90
Maths = 100
print(f"Rohan got {English+Hindi+Maths:.2f} out of 300 in the examination")

##(5) Errors while using f-string in Python
#In Python f-string, Backslash Cannot be used in format string directly.(Like Path declaration and all those things)
#  For escape sequences like \n for newlines or \t for tabs, they work fine within f-strings.
ram = 70
mohan = 80
sohan = 90
print(f"Total number of students are {ram+mohan+sohan} {'\n'} we are using a problem")

##(6) Using double curley braces in the python
Ayush = 51
Anshul = 96
Surendra = 45
print("The value of Ayush is {Ayush} and value of Anshul is {Anshul} and surendra got {{45}}only") 

##(7) Literal braces and interpolation
name = "Alice"
age = 30
print(f"{{name}}: {name}, {{age}}:{age}") 
##{name}: Alice, {age}:30 output
#when we use double braces then it will print the same string which we have inserted under the double curly braces