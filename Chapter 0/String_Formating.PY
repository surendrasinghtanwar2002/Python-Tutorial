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