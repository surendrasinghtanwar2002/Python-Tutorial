# In this section we will add an item in the dictionary and also use conditional base method to check whether the key is presented
#or not and if its present it will return output and true and return and it does not return true it will add the value


#By adding key and value directly in the dictionary without any conditional statement
my_dictionary = {
    "Full_Name": "Surendra Singh Tanwar",
    "Father_Name":"Vikram Singh Tanwar",
    "Mother_Name": "Meera Kanwar",
    "Contact_No": 9460824001
}
my_dictionary["AdharCardNo"]= 747474758585699 #This method will simply add the key and items in the existing dictionary
print(my_dictionary)


#Adding items with key and value in the dictionary using conditional methods
if "PanCard" in my_dictionary:
    print("There is a pancard key in the dictioanry",my_dictionary.get("PanCard"))
else:
    my_dictionary["PanCard"]= 85457717441444
    print("Your new pancard number is", my_dictionary.get("PanCard"),"", my_dictionary)


#The update() method will update the dictionary with the items from a given argument.
#  If the item does not exist, the item will be added.

first_dictionary = {
    
}
c= first_dictionary
if "Full_Name" and "Last_Name" and "FatherName" in first_dictionary:
    print("Your full name is",first_dictionary.get("Full_Name"), first_dictionary.get("Last_Name"),first_dictionary.get("FatherName"))

else:
    if(c != "Full_Name" and c != "Last_Name") and c != "FatherName":
        first_dictionary["Full_Name"]="Surendra Singh Tanwar"
        first_dictionary["Last_Name"] ="Tanwar"
        first_dictionary["FatherName"] ="Vikram Singh Tanwar"
    else:
        print("Your all item have been added succesfully")
print(first_dictionary)


###Second approach to create the empty dictionary and add item as per our requirement
blank_dictionary = {}
total_value = int(input("Enter your total number of input= "))

for i in range(total_value):
    key= input("Enter your key name= ")
    value = input("Enter your value= ")
    blank_dictionary[key]= value
    print("Dictionary have been updated  using user input =",blank_dictionary)

