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

## Updating dictionary existing key value with refering it key name
first_dictionary = {
    "First_Name": "Surendra Singh Tanwar",
    "Age": 24,
    "City": "Balotra",
    "Adhar_Card_no": 747474758589,
    "Pan_Card_No": 48887578585256
}
first_dictionary.update({"Age": 28})
print(first_dictionary)
