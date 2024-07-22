                                            ## Python Sets ##

#Sets are being used to store multiple item in a single variable
#Sets are a collection of unordered, unmutable and unindexed

### Basic Sets Practise ###

# (1) Creation of set 

#Approach 1 
myset = {"apple","banana","cheery","hotdogs","girafe","apple","banana"}
print(myset) #removing duplicate value and items are unordered

#Approach 2
myset1 = {"surendra","mohit","harish","kamlesh","jagdish","Surendra","surendra"}
print(myset1)

# Approach 3 (True and 1 and False and 0 is considered the same value)
myset3 = {"apple","banana","cherry",True,1,False,0}
print(myset3)

# (2) Finding the length of the set 

#Approach 1
myset4= {"surendra","kamlesh","harish","manish","Chandrapal"}
print(len(myset4))

#Approach 2
myset5 = {10,20,30,40,50,60,70,80,90,100,110,120,10}
print(len(myset5)) #As we know it will remove the duplicate items from the set

# (3) Set items - Data Types

#Approach 1
myset5 = {"Surendra",True,None,False,25.60,9460824001}
print(myset5)
print(len(myset5))

#Approach 2
myset6 = {"jagdish",0b001,10,20,30,40,50,60,40}
print(myset6)

mylist = list(myset6)
print(f"This is first item: {mylist[0]} and their type is {type(mylist[0])}")
print(f"This is first item: {mylist[1]} and their type is {type(mylist[1])}")
print(f"This is first item: {mylist[2]} and their type is {type(mylist[2])}")
print(f"This is first item: {mylist[3]} and their type is {type(mylist[3])}")
print(f"This is first item: {mylist[4]} and their type is {type(mylist[4])}")
print(f"This is first item: {mylist[5]} and their type is {type(mylist[5])}")
print(f"This is first item: {mylist[6]} and their type is {type(mylist[6])}")
print(f"This is first item: {mylist[7]} and their type is {type(mylist[7])}")


# (4) Set Constructor
my_list = [10,20,30,40,50,60,70,80,90,10,20,30,40,50,60,70,80,90]
my_set = set(my_list)
sorted_elements = sorted(x for x in my_set if isinstance (x, int ))
print(sorted_elements)















##Advance topic below
# myset = {"apple","banana","cherry"}
# print(myset)
# print(len(myset))
# my_container = list(myset)
# print(my_container[0])
# print(my_container[1])
# print(my_container[2])

# myset1 = {"apple","banana","cheery","hotdogs","apple","banana"}
# print(f"This is unsorted elements using no function {myset1}")
# my_final_set = sorted(x for x in myset1 if isinstance(x, str))
# print(f"This is sorted elements using the sorted function {my_final_set}")

