                                        ## Python Tuple ##

## Python- Update (Tuple)

#Change Tuple value (Python Tuple value cannot be change because it is immutable and unchagable)



#Updating value into the tuple using constructor list method 

#Approach 1
my_first_tuple = ("apple","banana","cherry")
my_list= list(my_first_tuple) #Converted into the list
my_list.append("surendra") #Added item into last position using append method
my_second_tuple = tuple(my_list) #Again converting list into the tuple
print(my_second_tuple)

#Approach 2
my_third_tuple = ("192.168.1.2","192.168.1.3","192.168.1.4","192.168.1.5","192.168.1.6")
print(f"Previous length of tuple {len(my_third_tuple)}")
my_second_list = list(my_third_tuple)
if  len(my_second_list) == 5 or len(my_second_list) == 6:
    my_second_list.append("192.168.1.7")
else:
    print("Not list is already full can't change anything")

#Again converting list into the tuple
my_fourth_tuple = tuple (my_second_list)
print(f"Updated length of the tuple is {len(my_fourth_tuple)}")

#Approach 3 
#Creating a tuple
my_first_tuple = ("Surendra","Singh",23,"Poornima","Bca",2024,"192.168.1.2",2024,"Poornima")

#Creating newlist newset variable to pass value in it
new_set = set()
new_list = []

#Creating a for loop and filtering our data
for item in my_first_tuple:
    if item not in new_set:
        new_set.add(item)
        if new_set not in new_list:
            new_list = list(new_set)
        
#Checking whether item is being added or not in the list and set 
print(new_list)

#Now shortlisting our data according to their datatype 
number_list = sorted([x for x in new_list if isinstance(x, str)])
alphabet_list = sorted([j for j in new_list if isinstance(j,int)])

updated_list = number_list+alphabet_list
print(updated_list)

#Approach 4 

my_first_tuple = ("apple","banana","cherry","apple","date","banana")

#creating a set variable to remove the duplicates value from the tuple
updated_set = set()

#Calling a loop to pass the tuple items into the set
for item in my_first_tuple:
    if item not in updated_set:
        updated_set.add(item)

#sort listing the set items into their ascending to descending order
sorted_set = sorted(updated_set, key = len)
print(sorted_set)

# Printing the results
print("Unique items:", unique_items)
print("Sorted list by length:", sorted_list)

#Approach 5

my_first_tuple = ("hello",42,"world","hello",100,"python")

##Removing duplicates value from the tuple
sorted_tuple = set (my_first_tuple)

##Converting the sorted_set into the list 
new_list = list(sorted_tuple)

#checking whether this item is presented in the list or not 
index_value = 0 
if "hello" in new_list:
    index_value=new_list.index("hello")
    new_list[index_value] = "hy"
else:
    print("Your given string is not presented in the list")

#sorting the list 
str_sorted_list = [sorted(x for x in new_list if isinstance(x, str))]
interger_sorted_list = [sorted(j for j in new_list if isinstance(j, int))]
final_list = str_sorted_list+interger_sorted_list
print(final_list)
