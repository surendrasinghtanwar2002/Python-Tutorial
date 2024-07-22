                                        ## Python Set Learning ##

## Python Joins Sets ##

#(1) union () method will Returns a new set containing all unique elements from the original set(s) involved.

#Approach (1) Passing one set at a time
my_set1 = {"apple","banana","cheerry","watermellon"}
my_set2 = {"surendra","manish","rakesh","jagdish"}
combined_set = my_set1.union(my_set2)
print(combined_set) ##It will combined both set and put into another set 

#Approach (2) Passing a list into the set
my_set42 = {"apple","banana","cheerry","watermellon"}
my_list2 = [10,20,30,40,50,60,70,80,90,100]
new_set=my_set42.union(my_list2)
print(new_set) #Passed a list into the tupple

#Approach (3) Passing two set at a time
my_set3 = {"Mohan","jagdish","rakesh","kamlesh","harish"}
my_set4 = {"Mohan","surendra","Kamlesh","Anshul","Ayush"}
my_set44 = {"Suresh","Mukesh","Khush","Imran","Gourav"}
combined_set1 = my_set3.union(my_set4,my_set44) #We can pass more then one set in union
print(combined_set1)

#Approach (4) Using the | operator, separate the sets with more | operators
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {11,12,13,14,15,16,17,18,19,20}
set3 = {21,22,23,24,25,26,27,28,29,30}
set4 ={31,32,33,34,35,36,37,38,39,40}
mixing_all_set = set1 | set2 | set3 | set4
print(mixing_all_set)

##Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

#(2) update() method and it changes the original set by adding elements from the other set(s).

#Approach (1) Passing set 
my_set5 = {"Rohit","Yash","Ayush","Shubhanshu","Ritik","Devnash"}
my_set6 = {"Lokendar","jagdish","khushvendar","Vicky","Aditya"}
my_set5.update(my_set6)
print(my_set5) ##It can add to existing set and can't create new set while using it

#Approach (2) Passing list
my_set7 = {"Rohit","Yash","Ayush","Shubhanshu","Ritik","Devnash"}
my_list1 = ["Lokendar","jagdish","khushvendar","Vicky","Aditya"]
my_set7.update(my_list1) #We are adding a list within the set using update method
print(type(my_set7))

#Approach (3) Passing multiple set at a time
my_set9 = {"Rohit","Yash","Ayush","Shubhanshu","Ritik","Devnash"}
my_set10 = {"Mohan","jagdish","rakesh","kamlesh","harish"}
my_set11 = {"apple","banana","cheerry","watermellon"}
my_set9.update(my_set10,my_set11)
print(my_set9)


#(3) intersection() method will return a new set that only contains the items which are presented in both sets.

#Approach 1 (Finding common value in integer value from two set)
my_set12 = {10,20,30,40,50,60,70,80,90,100}
my_set13 = {110,120,130,140,150,160,170,180,190,200,10,30,50}
comparing_set = my_set12.intersection(my_set13)
print(comparing_set)

#Approach 2 (Finding common value in strings from two set)
my_set14 = {"surendra","manish","rakesh","jagdish","khushvendar"}
my_set15 = {"jaimin","rohit","krishna","Gourav","khushvendar","surendra"}
common_name = my_set14.intersection(my_set15)
print(common_name)

#Approach 3 (Finding common_name and common value from multiple set)
my_set16 = {"apple", "banana", "cherry"}
my_set17 = {"google", "microsoft", "apple"}
my_set18 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
my_set19 = {110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 10, 30, 50}

common_thing = my_set16.intersection(my_set17, my_set18, my_set19)
print(f"These are the common elements present in all sets: {common_thing}")