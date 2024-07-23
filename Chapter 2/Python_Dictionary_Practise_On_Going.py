                                ### Python Dictionary Practise ###

## Basic Practise ##

#Practise 1:- (Printing Dictionary items)
thisdict= {
    "name":"Surendra",
    "Class": 12,
    "Mobile_no": 9460824001,
    "Subject": "Bca-Cloud",
    "Email-Address": "surendrasinghtanwar667@gmail.com"
}
print(thisdict["name"])
print(thisdict["Class"])
print(thisdict["Mobile_no"])
print(thisdict["Subject"])
print(thisdict["Email-Address"])

#Practise 2 (printing entire Dictionary at a time)
thisdict2 = {
    "name":"surendra",
    "Class": "Bca Cloud",
    "Mobile_no": 9460824001,
    "Subject": "Python Dictionary Class"
}
print(thisdict2)

#Practise 3 (Finding the len and type of the Dictionary)
thisdict3 = {
    "name":"Surendra",
    "Class": "Bca",
    "subject":"bca",
    "Mobile_no":9460824001,
    "Email-Address":"Surendrasinghtanwar667@gmail.com"
}
print(len(thisdict3))
print(type(thisdict3))

#Practise 4 (The values of the Dictionary items can be of any datatype)
thisdict4 = {
    "student_name": ["surendra","mohit","c"],
    "student_mobile_no": [9460824001,9460824001,9460824001],
    "married_status": False
}
print(thisdict4["student_name"])

#Practise 5 ("Extracting a single value from the entire list which stands in a single key")
thisdict5 =  {
    "student_name": ["surendra","mohit","c"],
    "student_mobile_no": [9460824001,8209269438,9414384439],
    "married_status": False
    }
temporary_storage = thisdict5["student_mobile_no"]
print(type(temporary_storage))
for item in temporary_storage:
    print(item)
    
#Practise 6 (Dictionary Constructor)

#Approach 1 (Creating a Dictionary from the nested list)
mydictionary1 = dict([["name","surendra"],["subject","bca"],["Mobile_no",9460824001]])
print(mydictionary1)

#Approach 2 (Creating a Dictionary from the tuple)
mydictionary2 = dict([("name","surendra"), ("Class", "bca"), ("subject","cloud-computing"), ("Mobile_no",9460824001)])
print(mydictionary2)

#Approach 3 (Creating a Dictionary from the set)
mydictionary3 = dict([{"name","surendra"},{"class","bca"},{"subject","cloud-computing"},{"Mobile_no",9460824001},{"roll_no",101}])
print(mydictionary3)

#Approach 4 (Creating a Dictionary from the keys and value pair)
mydictionary4 = dict(name="surendra",college_name = "Poornima University", Mobile_no=9460824001)
print(mydictionary4)

#Approach 5 (Dictionary Comprehension)
my_dict = dict((x, x**2) for x in range(5))
print(my_dict)# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


## Access Dictionary Items (Methods) ##

#Practise 1 (Access item using standard keys methods)
thisdict6 = {
    "name":"surendra",
    "class": "bca",
    "Mobile_no": 9460824001,
    "Email-Address": "Surendrasinghtanwar667@gmail.com"
}
print(thisdict6["name"])
print(thisdict6["class"])
print(thisdict6["Mobile_no"])
print(thisdict6["Email-Address"])

#Practise 2 (Access item using get() method where we will specify key in get method)
thisdict7 = {
    "name":"surendra",
    "Mobile_no": 9460824001,
    "class": "bca",
    "subject": "Bca-Cloud"
}
print(thisdict7.get("name")) #pass a key name as argument in get function
print(thisdict7.get("Mobile_no"))
print(thisdict7.get("class"))
print(thisdict7.get("subject"))

#Practise 3 (Extracting all the keys of the Dictionary using keys() method)
thisdict8 = {
    "car_name": "maruti suzuki 800",
    "car_model_year": 2018,
    "car_price": 1.50,
    "car_owner_name": "Surendra Singh Tanwar"
}
all_keys = thisdict8.keys()
print(type(all_keys))
print(all_keys)

#Practise 4 (Extracting all the value of the Dictionary using values() method)
thisdict9 = {
    "car_name": "maruti suzuki 800",
    "car_model_year": 2018,
    "car_price": 1.50,
    "car_owner_name": "Surendra Singh Tanwar"
}
all_values = thisdict9.values()
print(f"Datatype of all_values variable is : {type(all_values)}")
print(f"This is the exact value which is being extract from the Dictionary: {all_values}")















