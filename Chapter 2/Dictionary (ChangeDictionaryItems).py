# In this section we will practise to change means add delete or update the existing key and values in the dictionary


##Adding new item by referring to its key name and key value:
my_dictionary = {
    "Model_Name": "Surendra Singh Tanwar",
    "Age": 24,
    "Course": "Bca",
    "City": "Balotra",
    "Contact_No": 9460824001
}
print(len(my_dictionary)) ##Total items in the dictionary is now 5

my_dictionary["Email_Address"]= "surendrasinghtanwar667@gmail.com"
print(my_dictionary)
print(len(my_dictionary)) ##Total items in the dictionary after updating is 6

## Updating dictionary existing key value with refering it key name if there is a key present so it will update either it will create the key with the value in the dictionary
first_dictionary = {
    "First_Name": "Surendra Singh Tanwar",
    "Age": 24,
    "City": "Balotra",
    "Adhar_Card_no": 747474758589,
    "Pan_Card_No": 48887578585256
}
first_dictionary.update({"Age": 28})
first_dictionary.update({"Class": 12})
print(first_dictionary)


## Updating dictionary keys and values with nested if else condition to check whether the key is presented or not
second_dictionary = {
    "First_Name": "Surendra",
    "Middle_Name": "Singh",
    "Last_Name":   "Tanwar",
    "Age": 24,
    "Course": "BCA",
    "Occupation": "Devnet Engineer"
}
print(len(second_dictionary))

#checking whether course is bca
c = second_dictionary["Course"]
print(c)
if (c=="Arts"):
    print("Your course is BCA")
else:
   second_dictionary["Course"] = "Arts"
   print(second_dictionary)



## Practical project using nested if else and change existing value of the key
my_dictionary = {
    "Full_Name":"Surendra Singh Tanwar",
    "Course":"Bca",
    "MobileNo": 9460824001,
    "Finding_Job": False,
    "Resume_Attached": True
}
a = my_dictionary["Finding_Job"]
b = my_dictionary["Resume_Attached"]
if(a == True):
    print("Yaaa he is finding the job right now")
else:
    if(b == True):
        my_dictionary["Finding_Job"]= True
        print("We have found that his resume is being attached so he is finding job")
        print(my_dictionary)
    else:
        print("He is not interested because his resume and finding both are false")
