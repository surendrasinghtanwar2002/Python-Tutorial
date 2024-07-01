# In this section we will practise dictionary from scratch (Beginner)
my_dictionary = {
    "name": "Surendra Singh Tanwar",
    "Course": "BCA",
    "Contact No": 9460824001,
    "Occupation": "Devnet Engineer",
    "University": "Poornima University"
}
print(my_dictionary) #Printing the dictionary
print(len(my_dictionary)) #finding the length of dictionary
print(type(my_dictionary)) #This is dictionary class


## In this we will basically print each item of the dictionary
second_dictionary = {
    "Name": "surendra singh tanwar",
    "Graduation": "Bca Cloud Computing",
    "Mobile no": 9460824001,
    "Mail Address": "Surendrasinghtanwar667@gmail.com",
    "Married": False
    }
print(second_dictionary["Name"].title())
print(second_dictionary["Graduation"])
print(second_dictionary["Mobile no"])
print(second_dictionary["Mail Address"].lower())
print(second_dictionary["Married"])

#In this section we will find that duplicate value are not allowed
third_dictionary = {
   "Brand":"Maruti",
   "Model": "Maruti Suzuki 800",
   "Year": 1998,
   "Year": 2000
}
print(third_dictionary) #When we have given same key to both it will replace to new key with value

#In this section we will practise that how we can create tuple from the dictionary values or items
car_manufacturing = {
    "Car_Brand": "tata",
    "Car_Model": "tata nexon",
    "Manufacturing_year": 2006,
    "Owner": "Ratan Tata"
}
print(car_manufacturing)
c = car_manufacturing["Car_Brand"],car_manufacturing["Car_Model"],car_manufacturing["Manufacturing_year"],car_manufacturing["Owner"]
print(c) #It will give output of value of the dictionary 
print(type(c)) #Now it have been converted into the tuple
print(c[0]) #Print first index value "tata"
print(c[1]) #print second index value "tata nexon"
print(c[2]) #print third index value 2006
print(c[3]) #print fourth_index value Ratan Tata
print(("So recently",c[3],"the owner of",c[0].title(),"company have launched a car",c[1].title(),"in the year of",c[2]))

#In this section we will practise dictionary length len() function to check the length
fourth_dictionary= {
    "FullName": "Harish Kumar Chanchad",
    "Father_Name":"Ramesh kumar Chanchad",
    "Mother_Name": "Fula Devi",
    "Contact Number": 9460824001,
    "Married": False,
    "Adhar_Card_no": 7474747474747474,
    "Bank_Account_no": 898989889898989
}
print(fourth_dictionary)
print(len(fourth_dictionary)) #find total number of items in the list


#In this section we will practise dictionary items can be of any datatypes
fifth_dictionary = {
    "Brand": "Intel",
    "Manufacturing_Year": 1998,
    "Owner": "Harish kumar Chandanani",
    "Contact": "intelharishparmani@gmail.com",
    "IntelModel":["I3","I5","I7","I9"],
    "Graphic_Card":{
        "Budget": "RTX 3090",
        "Mid_Range": "RTX 4090",
        "Best_Performance": "RTX 6090",
        "God_Level_Performance": "RTX 10090"
                    },
    'Lucky_number':[1,3,5,9,11,16,17,19,25,36,450,250,750,980]
}
print(fifth_dictionary)
c = fifth_dictionary["Lucky_number"]
print(type(c))  #Now it become list because it has only numerical value
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])
print(c[5])
print(c[6])
print(c[7])
print(c[8])
print(c[9])
print(c[10])
print(c[11])
print(c[12])
print(c[13])  # In this we are priting each index value number by printing each number line by line

for i in c: #we basically print the entire c using one loop
    print("from the loop we are priting entire list at a single time",i)

d = fifth_dictionary["Graphic_Card"]
print(type(d))
print("There are multiple options",d["Budget"],d["Mid_Range"],d["Best_Performance"],d["God_Level_Performance"])