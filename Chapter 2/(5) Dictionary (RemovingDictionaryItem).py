# In this section we will basically remove the items from the dictionary

#First step (Basic methods)


#pop() method by using this method we can remove any item any passing a key name as argument for removing from the dictionary
my_dictionary= {
    "Full_Name": "Surendra",
    "Mid Name": "Singh",
    "Last_Name": "Tanwar",
    "Contact_no": 9460824001,
    "Married": False
}
# print(my_dictionary, len(my_dictionary), type(my_dictionary))
my_dictionary.pop("Full_Name")
print(my_dictionary)


#popitem() method by using we can remove the last item from the dictionary
first_dictionary = {
    "First_Name": "Surendra Singh Tanwar",
    "Mobile_No": 9460824001,
    "Father_Name": "Vikram Singh Tanwar",
    "Occupation": "Network Engineer"
}
first_dictionary.popitem() # so this will basically last item from the dictionary which is occupation
print(first_dictionary)

#del method is being used to remove specific items from the dictionary using key name and we can also remove the entire dictionary using this del method
second_dictionary = {
    "First_Name": "Surendra Singh Tanwar",
    "Father_Name": "Vikram Singh Tanwar",
    "Mobile_no": 9460824001,
    "EmailAddress": "surendrasinghtanwar667@gmail.com"
}
del second_dictionary["EmailAddress"] ## now it have removed specific email address item from the list
print(second_dictionary)

# using del method to remove the  entire dictionary with all keys and values from the list 
third_dictionary = {
    "First_Name": "Surendra Singh Tanwar",
    "Father_Name": "Vikram Singh Tanwar",
    "Mobile_No": 9460824001,
    "Email": "surendrasinghtanwar667@gmail.com"
}
print(third_dictionary)

del third_dictionary
print(third_dictionary)  ##It will give error because we have removed the entire dictionary from the program