### Loop through a dictionary### 

#We can loop a dictionary through a dictionary (Basic)

#printing all the keys names in the dictionary, one by one 
my_dictionary={
    "First_Name":"Surendra Singh Tanwar",
    "Father's_Name":"Vikram Singh Tanwar",
    "Mobile_no": 9460824001,
    "Email_Address": "surendrasinghtanwar667@gmail.com"
}
print(my_dictionary)
for i in my_dictionary:
    print("My dictionary entires key",i)

##Printing all the value one by one of any dictionary

#first methods
second_dictionary={
    "First_Name":"Surendra Singh Tanwar",
    "Father's_Name":"Vikram Singh Tanwar",
    "Mobile_no": 9460824001,
    "Email_Address": "surendrasinghtanwar667@gmail.com"
}
for i in second_dictionary:
    print(second_dictionary[i])

#second methods
for i in second_dictionary.values():
    print(i)


#priting all the keys of the dictionary one by one
fourth_dictionary = {
   "First_Name":"Surendra Singh Tanwar",
    "Father's_Name":"Vikram Singh Tanwar",
    "Mobile_no": 9460824001,
    "Email_Address": "surendrasinghtanwar667@gmail.com"
}
for i in fourth_dictionary.keys():
    print("Fifth_dictionary keys:",i)

#printing all the values of the dictionary one by one
fifth_dictionary = {
    "First_Name":"Surendra Singh Tanwar",
    "Father's_Name":"Vikram Singh Tanwar",
    "Mobile_no": 9460824001,
    "Email_Address": "surendrasinghtanwar667@gmail.com"
}
for i in fifth_dictionary.values():
    print("Fifth_dictionary values:", i)

#Printing all the keys and value of the dictionary one by one
third_dictionary = {
    "First_Name":"Surendra Singh Tanwar",
    "Father's_Name":"Vikram Singh Tanwar",
    "Mobile_no": 9460824001,
    "Email_Address": "surendrasinghtanwar667@gmail.com"
}
for i,x in third_dictionary.items():
    print(str(i),":",str(x))
