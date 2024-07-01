### In this section we will practise that how to access the items of any dictionary ###
my_dictionary ={
    "Full Name": "Surendra Singh Tanwar",
    "Father_Name": "Vikram Singh Tanwar",
    "Occupation": "Devnet Engineer",
    "Course": "Bca Cloud",
    "Contact_no": 9460824001
}
print(my_dictionary)

### We can also use "get()" method to pick any items from the dictionary ###
c = my_dictionary.get("Full Name")
print(c.upper())

d = my_dictionary["Father_Name"] #Traditional method to pick any item from the dictionary 
print(d.upper())

### We can use "keys()" method to return a list of all the keys in the dictionary 
first_dictioanry ={
    "Book_Name": "2 States",
    "Book_Author": "Chetan Bhagat",
    "Spoiler":"Surendra Singh Tanwar",
    "Date of Manufacturer": 1998
}
print(first_dictioanry)
c = first_dictioanry.keys()
print(c)


### We can use "values()" methods to return a list of all the values in the dictionary
second_dictionary={
    "Name": "Surendra Singh Tanwar",
    "Mobile no": 9460824001,
    "Email_Address": "surendrasinghtanwar667@gmail.com",
    "Course":"BCA",
    "Subject": "Cloud Computing",
    "Roll_no":[78,89,14,16,56,54,25,36,75,85],
    "Additional_Details":{
        "Adhar_Card_no": 7979797979797,
        "Account_no": 4641616156118
    }
}
print(second_dictionary)
d = second_dictionary["Additional_Details"]
print(type(d))
x = second_dictionary.values()
print(x)


### We can use "items()" method to get all the items  present in the dictioanry
z = second_dictionary.items() #It only add () bracket to each items to make seperate
print(z) #We can print using direct print method instead of getting items methods
print(second_dictionary)


## We can also check the key if its exist in the dictionary or not
third_dictionary ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "brand" and "model" in third_dictionary:{
    print("Yes there is a key name with brand exist")
}
else:
    print("There is no brand present in the dictionary")

#We can also check the key if its exist then print and if doesn;t exist then we add that items or key in the list
if ("condition" in third_dictionary):
    print("Yes there is a condition key avilable in the dictionary")
else: 
    third_dictionary["condition"] = "New Car"
    print(third_dictionary)

fourthdictionary = {
    "Name": "Surendra Singh Tanwar",
    "Class": 12,
    "Course": "BCA",
    "Occupation": "DevNet Engineer",
    "Country": "India",
    'Married': True,
}
print(len(fourthdictionary))
if "Additional_Details" in fourthdictionary:{
    print("Your Additional details are present in the dictionary")
}
else:
    fourthdictionary["Addtional_Details"] = {
        "Account_No": 787878787788,
        "PanCardno": 445454544545,
        "Licenceno": 44484818181699          
     }
print(fourthdictionary, len(fourthdictionary)) 

if all (fourthdictionary.values()):  #all method will check entire dictionary items that are true if one of it are false then it will give else statement output otherwise true
    print("Your value is be true")
else:
    print("Your value is not true")