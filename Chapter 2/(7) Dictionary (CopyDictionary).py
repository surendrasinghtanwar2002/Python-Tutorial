## In this section we will practise Python-Copy Dictionaries


#First method using "copy()" method which will allow us to copy the entire dictionary into another variable
First_dictionary = {
    "Model_Name": "Surendra Singh Tanwar",
    "Age": 24,
    "Course": "Bca",
    "City": "Balotra",
    "Contact_No": 9460824001
}
new_dictionary = First_dictionary.copy()
print(new_dictionary)
print(type(new_dictionary))

#Second method using dict() method which is another way to make a copy is to use the built in function
second_dictionary = {
   "Model_Name": "Surendra Singh Tanwar",
    "Age": 24,
    "Course": "Bca",
    "City": "Balotra",
    "Contact_No": 9460824001
}
mydict = dict(second_dictionary)
print(mydict, type(mydict))