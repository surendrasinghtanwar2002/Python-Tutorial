                ##List are mutable and orderable which means whatever we add it will add in the list

                                ##Creating a list and printing
thislist = ["apple","banna","cherry"]
print(thislist)

                                ##Allow duplicates sine list are indexed, list can have items with the same value
thislist1 = ["apple","banna","apple","grapes"] #As we can see we have duplicates elements
print(thislist1)

                                ##List various datatype in single List
thislist2 = ["Surendra",9460824001,True,45.60]
print(thislist2)
print(thislist2[0])
print(thislist2[1])
print(thislist2[2])
print(thislist2[3])

                                ##type() method to check the datatype of the variable
thislist3 = [1,6,5,8,9,7,10,5,63,25,45,63]
print(type(thislist3))

                                ##Constructor list
#Converting set into the list
Constructor_list = list({1,2,3,4,5,6,7,8,9,9,1,00,2,0,3,356,})
print(Constructor_list)

#Constructing set items into the list 
Constructor_list1 = list({1,2,3,4,5,6,7,"Surendra",True})
print(Constructor_list1)

#Constructing a dictionary into the list
Constructing_list2 = list({"Name":"Surendra","Class":12,"Contact_no":"44564446464"})
print(Constructing_list2)

#Constructing a range into the list
Constructing_list3 =list(range(1,5+1))
print(Constructing_list3)

#Constructing a string into the list
Constructing_list4 = list("Hello")
print(Constructing_list4)
print(Constructing_list4[0])
print(Constructing_list4[1])
print(Constructing_list4[2])
print(Constructing_list4[3])
print(Constructing_list4[4])
Constructing_list4[4] ="I"
print(Constructing_list4)
Constructing_list4[3] = "H"
Constructing_list4[2] = "O"
Constructing_list4[1] = "P"
Constructing_list4[0] = "K"
print(Constructing_list4)


                            ##Python Acess List items

#Accessing items of the list via the index value
thislist4 = ["apple","banna","cherry"]
print(thislist4)
print(thislist4[0]) #index 0
print(thislist4[1]) #index 1
print(thislist4[2]) #index 2 

#Negative index
thislist4 = ["Surendra","rohan","mohan","kamlesh","sohan"]
print(thislist4[-1]) #index 5 "sohan"
print(thislist4[-2]) #index 4 "kamlesh"
print(thislist4[-3]) #index 3 "mohan"
print(thislist4[-4]) #index 2 "rohan"
print(thislist4[-5]) #index 1 "surendra"
print(thislist4[-5:-1]) #When we give range last value is n so in range it will be (n-1)
print(thislist4[-5:-2]) #it will give mohan last because n-1 
print(thislist4[-5:-3]) #it will give rohan last because n-1
print(thislist4[-5:-4]) #it will give surendra last because n-1
print(thislist4[-5:-5]) # It will be blank []

#Range of index
thislist5 = ["apple","banna","cherry","grapes","watermelon",'kiwwi',"dragonfruit","mango"]
print(thislist5[0:5]) 
print(thislist5[:6]) #It will take by default 0 as starting index
print(thislist5[2:]) #It will take by default last as ending index
print(thislist5[1:6])

#Range of Negative index
thislist5= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist5[-4:-1]) ##last range n-1

thislist6 = ["Surendra","Rohan","Mohan","kamlesh","Ganesh","Sohan"]
print(thislist6)
print(len(thislist6))
print(thislist6[-4:-2])

                        ##Check if items exist in the list or not
#First Approach
thelist7 = ["Mohan","Kamlesh","Sohan","Jagdish","Rohit","Jatin"]
print(thelist7)
if "surendra" in thelist7:
    print("Hurray we have found the Kamlesh")
else:
    print(f"Pagal wagal hai kya kha hai surendra")
    
thislist8 = ["Manish","Manisha","Ayushi","Aditi","Pranidhi"]
print(thislist8)

#Second Approach
if "Manisha" in thislist8:
    index = thislist8.index("Manisha")
    thislist8[index] = "Mohini"
    print("You have done")
else:
    print("Your item have not been changed")
print(thislist8)

#Third Approach
if "Manish" in thislist8:
    index = thislist8.index("Manish")
    thislist8[index] ="Manish is a good boy"
    print("You have done")

else:
    print("Not person with Manish have been found")
print(thislist8)

#Fourth Approach

#List of the user
# thislist9 = ["Kamlesh","Mohan","Jagdish","Suresh",'Harish',"Pratik","Amol"]

# userinput = input("Enter your value you have to find in the list = ")
# change_input = input(f"You have selected {userinput} so what you have to in this = ")
# if userinput in thislist9:
#     index_value = thislist9.index(userinput)
#     thislist9[index_value] = change_input
#     print("Your statement have been update")
# else:
#     print("Your statement have not been updated")

# print(thislist9)

                                    ##Change Item value

#Changing specific items in the list
thislist10 = ["Apple","banana","grapes"]
print(thislist10[0])
thislist10[0] = "watermelon"
print(thislist10)

#Changing a range of items which exist in the list 
thislist11 = ["Apple","banna","watermelon","grapes",'Rakesh',"Mukesh",'Jagdish']
print(thislist11[0:4])

thislist11[0:4] =["Surendra","Mohan","Sukesh","Elon Musk"]
print(thislist11)
print(len(thislist11))

#The length of the list will be change when the number of items inserted does not match

#Approach(1)
thislist12 = ["Kamlesh","Suresh","Jagdish",'Irfan',"Imran"]
print(len(thislist12)) #Length of the list is 5

thislist12[0:2+1]= ["Surendra"] #I have input one item from 0 to 3 range when there was already 3 items exist
print(thislist12) #Now Length of the list is 3 because we have changed the list12 range from 5 to 3

#Approach(2)
thislist13= [10,20,30,40,50,60,70,80,90,100]
print(thislist13)
print(len(thislist13)) #Length of the list is 10
thislist13[0:4] =[10]
print(thislist13)
print(len(thislist13))

                        ##Insert Item and Append Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:
#Approach(1)
thislist14 = ["Surendra","Mohan",'Kamlesh',"Jagdish","Sukhvinder","Magvinder"]
print(thislist14)
print(type(thislist14))
print(len(thislist14))
thislist14.insert(4,"Mukesh")
print(thislist14)

#Approach(2)
thislist15 = ["Mukesh","Jagdish","Kamlesh","Rohan","Mansish","Chandrapal","Subhanshu"]
print(thislist15)
print(len(thislist15)) ##List length is 7
thislist15.insert(3,"Stop waiting for sometime")
print(thislist15)

#Approach(3)
thislist16 = ["Suresh","Mansish","Jagdish","Kamlesh","Sukesh","Kapil","Komal"]
print(thislist16)
thislist16.insert(5,"Good to Go")
print(thislist16)

##Append() method is being used to add items to the end of the list 
stack  = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
last_item = stack.pop()
print(last_item)
print(stack)

#Approach 1
stack_list = [1,2,3,4,5,6,7,8,9,10]
print(stack_list)
print(len(stack_list))
stack_list.append(11) ##We are adding a items in the last elements
print(stack_list)

#Approach 2
stack_list2 = [10,20,30,40,50,60,70,80,90,100]
print(stack_list2)
print(len(stack_list2)) #At initialise stage length of stack_list2 is 10
stack_list2.append(110) #Adding items in the list from end of the list 110
print(stack_list2)
print(len(stack_list2)) ##After adding item in the list length of the list is 11

##Extend method
#To append elements from another list to the current list, use the extend() method.
list_1 = [10,20,30,40,50,60,70,80,90,100]
list_2 =[110,120,130,140,150,160,170,180,190,200]
print(list_1)
print(list_2)
print(len(list_1)) #Length of the list is 10
print(len(list_2)) #Length of the list is 10
print(id(list_1)) #finding the memory block id of the list_1
print(id(list_2)) #finding the memory block id of the list_2
new_list = list_1+list_2 #It is used when we have to add two list and form one new list
list_1.extend(list_2) #It is being used to add another iterable items or list in the existing list
print(new_list)
print(list_1)

##Add any iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist17 =["Suresh","Mukesh","Jagdish","Ramesh","Manish"]
print(id(thislist17))
fruits = ("Apple","banana","Cherry",'Mango',"watermelon")
thislist17.extend(fruits) ##adding or extending a tuple into the list
print(id(thislist17))
my_dictionary= {"id":1,"name":"Surendra Singh Tanwar","Mobile no": 9460824001} #created a dictionary for extending into my list
print(my_dictionary)

thislist17.extend(my_dictionary.values()) #passing my_dictionary as argument and adding values only
print(thislist17)

my_string = "Surendra"
thislist17.extend(my_string)
print(thislist17)

                                ##Python-Remove List Items
##remove() function is used to remove specific items name from the List

#Approach 1
student_list = ["Surendra","Mohan","Rakesh","Jagdish","Suresh","Manish"]
student_list.remove("Mohan")
print(student_list)

#Approach 2
student_list_1 = ["Manish","Suresh","Jagdish","Khushvendar","Gourav","Devansh"]
print(student_list_1)
student_list_1.remove("Suresh")
print(student_list_1)

#Approach 3 If there are more than one item with the specified value, the remove() method removes the first occurrence:
student_list_2 = ["Mohan","Kamlesh","Rakesh","Jagdish","Mohan","Surendra"]
student_list_2.remove("Mohan")
print(student_list_2)

##Pop() method will remove the specific index 
#Approach 1 using index value
student_list_3 = ["apple","banana","Cherry","grapes"]
student_list_3.pop(0)
print(student_list_3)

#checking who is on 0 index Now
student_list_3.pop(0)
student_list_3.pop(0)
student_list_3.pop(0)
print(student_list_3)

#Approach 2 using no argument and if we will not pass argument it will remove the last elements from the List
class_list = ["class-1","class-2","class-3","class-4","class-5"]
class_list.pop() #It will automatically take the last elements
print(class_list)


##del() method is also used to remove the specific index value:

#Approach 1 removing specific items from the list 
my_diary = ["James","Johnson","Kali","One man army","Jagdish Bhagat"]
print(my_diary)
del my_diary[0] ##removing 0 index from the list
print(my_diary)

#Approach 2 removing entire list from the list
my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)
del my_list
# print(my_list) #It will through error because you have remove the list before using del method


##clear() method is being used to remove the items from the list 
my_list_1= [0,2,55,6,5,8,96,5,2,10]
print(my_list_1)
my_list_1.clear()
print(my_list_1) ##output [] because we have cleared every single items from the list


                                        ##Python Loop
                            
                            ## Priting list using for loop ##
                            
#We can loop through the list items by using a for loop:
personal_list = [1,3,4,5,6,7,89,10]
for i in personal_list:
    print(i)

#Priting the index value through the len and looping statement
personal_list_1 = [10,20,30,40,50,60,70,80,90,100]
print(personal_list_1)
for i in range(len(personal_list_1)):
    print(i)
    
#Printing the index and value combined using enumerate function

#It will unpack the list because list is packed with index and value so it will unpack
#the list and first it will take index and put into the variable and Second it will take value and put into the variable
#It will track the index value while iterating sequence of the list
personal_list_2 = [10,20,30,40,50,60,70,80,90,100]
for list_index, list_value in enumerate(personal_list_2):
    print(f"index{list_index} and value is {list_value}")


                                    ## While Loop ##
fruits = ["banana","grapes","orange","apple"]
print(fruits)
i = 0 #starting index
while i <len(fruits): #specific len of the fruits:
    print(fruits[i])
    i = i+1

