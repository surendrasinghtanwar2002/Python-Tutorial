                                ## Python Access Dictionary Items ##

    ##Accessing Items##

#Tradition Method for Accessing items of the Dictionary using key Method

#Approach 1
thisdict = {
    "name":"surendra",
    "class":"12th bca",
    "subject": "bca",
    "college": "poornima university"
}
print(thisdict["name"])

#Accessing items using get method to give the same result 

#Approach 1 
thisdict1 = {
    "name":"surendra",
    "class":"Bachelors",
    "subject":"BCA",
    "CONTACT_NO": 9460824001
}
print(thisdict1["name"])

#Keys() method to return all the keys which are present in the Dictionary

#Approach 1 
thisdict2 = {
    "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
}
myname = thisdict2.keys()
print(type(myname))
print(myname)

#Approach 2 *Finding all the keys and changing their value after getting the keys name

thisdict2["carmodelname"] = "hyundai"
print(thisdict2["carmodelname"])

#values () method will return all the values which are present in the Dictionary

#Approach 1
thisdict3 = {
    "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
}
print(thisdict3.values())

#Approach 2 *Finding all the values and changing their value after getting the values of keys
thisdict4 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
    
##This is extra part don't focus on it
valueholding = ((x, y) for x, y in enumerate(thisdict4))  
for i,y in valueholding:
    print(i,y)

thisdict4["car_warranty"] = 8
print(thisdict4)

#items () method will return both keys and value from the Dictionary
thisdict5 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
returnvalue = thisdict5.items()
print(type(returnvalue))

#check if key exist in the Dictionary

#Approach 1 
thisdict5 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
value_return = 1 if "carmodelname" in thisdict5 else 0 ##checking condition only
value_return1 = [items for items in thisdict5 if "carname" in thisdict5]
print(value_return1)
print(bool(value_return))

        ##Change Dictionary items##

#changing value of the Dictionary items using Traditional method called their key name

#Approach 1
thisdict5 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
thisdict5["carname"] ="dzire" #changing value with key name
print(thisdict5)

#Approach 2
thisdict6 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
thisdict6["car_manufacturing_year"] = 2018 ##changing value with key name
print(thisdict6)

#changing or updating items using update() method

#Approach 1
thisdict7 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
thisdict7.update({"carname": "hyundai","carmodelname":"ferazi"})
print(thisdict7)


        ##Add Dictionary Items##

#Traditional method using key name

#Approach 1
thisdict8 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
thisdict8["car_manufacturing_year"] = 2019
print(thisdict8)

#using update method if you update value and if doesn;t exist it will add that item in your Dictionary

#Approach 1
thisdict9 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
thisdict9.update({"car_ownername":"surendrasingh"}) #if update method is not able to find that place it will add new items in the Dictionary
print(thisdict9)
    

        ##Remove Dictionary items##    

#pop method to Remove dictionary item using the key name

#Approach 1
thisdict10 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
thisdict10.pop("carname")
print(thisdict10)

#Approach 2 REMOVING ITEMS USING conditional base
thisdict11 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
if "carname" in thisdict11:
    thisdict11.pop("carname")
else:
    print("There is not such key carname present in the dictionary")
##conditional statement over here
print(f"This is the new dictionary return after the conditional statement {thisdict11}")

#popitem() method removes the last inserted item

#Approach 1
thisdict12 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
thisdict12.popitem() ##It will remove items from the last position
print(thisdict12)

#Approach 2
thisdict13 = {
     "carname":"maruti_suzuki",
    "carmodelname": 800,
    "car_manufacturing_year": 2012,
    "car_warranty": 5
    }
thisdict13.popitem()
print(thisdict13)

#del() method will remove the items using key and it can also remove entire dictionary

#Approach 1
user_data = {
    "Ip_Address": "192.168.1.2",
    "User_Location": (20,30),
    "Victim_Email_Address": "victim212@gmail.com",
    "victim_pc_configuration": "intel i7"
}
del user_data["Ip_Address"] ##It will remove the item from the dictionary
print(user_data)
del user_data ##It will remove the entire dictionary from the project
# print(user_data) ##Gives you error because no such kind of dictionary is avilable there
    
#clear() method will clear all the entries which are present in the dictionary

#Approach 1
user_data = {
    "Ip_Address": "192.168.1.2",
    "User_Location": (20,30),
    "Victim_Email_Address": "victim212@gmail.com",
    "victim_pc_configuration": "intel i7",
    "Tracking_position": "Active",
    "Mobile_No": 94225212455
}
user_data.clear()
print(user_data)

#Approach 2
user_data2 = {
    "Ip_Address": "192.168.1.2",
    "User_Location": (20,30),
    "Victim_Email_Address": "victim212@gmail.com",
    "victim_pc_configuration": "intel i7",
    "Tracking_position": "Active",
    "Mobile_No": 94225212455,
    "Camera_Access": True
}
user_data2.clear()
print(user_data2)
    
        ## Python Loop dictionary ##

#Loop through for loop

#Approach 1 (printing both keys and value using items method)
user_data2 = {
    "Ip_Address": "192.168.1.2",
    "User_Location": (20,30),
    "Victim_Email_Address": "victim212@gmail.com",
    "victim_pc_configuration": "intel i7",
    "Tracking_position": "Active",
    "Mobile_No": 94225212455,
    "Camera_Access": True
}
for x,y in user_data2.items():
    print(f" {x} || {y}")

#Approach 2 (printing only keys of the dictionary)
user_data3 = {
    "Ip_Address": "192.168.1.2",
    "User_Location": (20,30),
    "Victim_Email_Address": "victim212@gmail.com",
    "victim_pc_configuration": "intel i7",
    "Tracking_position": "Active",
    "Mobile_No": 94225212455,
    "Camera_Access": True
}
print("This all are keys of the dictionary:- ")
for key_data in user_data3.keys():
    x = key_data.expandtabs(40)  # Using 4 spaces for each tab
    print(x)
    
#Approach 3 (printing only values of the dictionary)    
user_data3 = {
    "Ip_Address": "192.168.1.2",
    "User_Location": (20,30),
    "Victim_Email_Address": "victim212@gmail.com",
    "victim_pc_configuration": "intel i7",
    "Tracking_position": "Active",
    "Mobile_No": 94225212455,
    "Camera_Access": True
}
for valuesofdictionary in user_data3.values():
    print(valuesofdictionary)
    
#Approach 4 (printing only keys of the dictionary)
user_data4 = {
    "Ip_Address": "192.168.1.2",
    "User_Location": 20,
    "Victim_Email_Address": "victim212@gmail.com",
    "victim_pc_configuration": "intel i7",
    "Tracking_position": "Active",
    "Mobile_No": 94225212455,
    "Camera_Access": True
}
#declaring a variable here
x=0
y = 0
for keys_data, value_data in user_data4.items():
    # print(keys_data,value_data, end = "*") ##end with working here
    if keys_data == str and value_data ==str:
        keys_data.upper()
        value_data.upper()
    print(keys_data,value_data)

print(x,y)

my_list = [10,20,30,40,50,60,70,80,90,100]
new_list = my_list.copy()
new_list[0] = 1000
print(my_list)
print(new_list)


    ##  Python-Copy dictionary ##

#Traditional method with = assignment operator to assign value into another variable but it will be only create a reference of it
#Approach 1
user_data4 = {
    "Ip_Address": "192.168.1.2",
    "User_Location": 20,
    "Victim_Email_Address": "victim212@gmail.com",
    "victim_pc_configuration": "intel i7",
    "Tracking_position": "Active",
    "Mobile_No": 94225212455,
    "Camera_Access": True
}
new_user_data = user_data4 ##Making a shallow copy of the entire dictionary
print(id(user_data4))
print(id(new_user_data))

new_user_data["Ip_Address"] ="192.168.1.3" #changes in the dictionary

print(f"This is old data = {user_data4}")
print(f"This is new data = {new_user_data}")

#Copy method in dictionary is used to make a clone of the dictionary it will not create the deep copy

#Approach 1
user_data8 = {
    "Ip_Address": "192.168.1.2",
    "User_Location": 20,
    "Victim_Email_Address": "victim212@gmail.com",
    "victim_pc_configuration": "intel i7",
    "Tracking_position": "Active",
    "Mobile_No": 94225212455,
    "Camera_Access": True
}
new_data_variable = user_data8.copy()
print(id(user_data8))
print(id(new_data_variable))

#Approach 2 (cello copy issue in nested elements)
user_data9 ={
    "Ip_Address": "192.168.1.2",
    "User_Location": 20,
    "Victim_Email_Address": "victim212@gmail.com",
    "victim_pc_configuration": "intel i7",
    "Tracking_position": "Active",
    "Mobile_No": 94225212455,
    "Camera_Access": True,
    "user_login_time_Record": [10,20,30,40,50,60,70]
}
new_data_of_user = user_data9.copy()
print(id(new_data_of_user))
new_data_of_user["user_login_time_Record"].append(5000)
print(user_data9)
print(new_data_of_user)

#make a copy of the dictionary using dict() constructor or a method in Python
my_user_data = {
    "name":"Surendra Singh Tanwar",
    "Mobile no": 9460824001,
    "Subject":"Bca",
    "Classes": "Bachelors"
}
new_dictionary = dict(my_user_data)
print(new_dictionary)

        ##Nested dictionary ##
#Creating a Nested dictionary and Accessing value of it 
my_user_data = {
    "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(my_user_data["child1"]["year"]) ##Accessing specific nested dictionary items
for i in my_user_data["child1"].items():
    print(f"This is the items which are present in {str(i)}")

#Extracting both items using loop through nested dictionaries
for key,obj in my_user_data.items():
    print(key)
    print(obj)
    for y in obj:
        print(y + ":", obj[y])














   
    
