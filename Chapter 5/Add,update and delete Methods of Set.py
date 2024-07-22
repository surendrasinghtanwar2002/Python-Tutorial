                                            ## Python Sets ##

#Sets are being used to store multiple item in a single variable
#Sets are a collection of unordered, unmutable and unindexed

### Access Set items Practise ###
thisset = {"apple","banana","grapes","mango","watermelon"}
for x in thisset:
    print(x)
    
thisset = {"apple","banana","mango","cherry"}
print("banana" in thisset)
print("apple" in thisset)
print("mango" in thisset)
print("cherry" in thisset)
print("hotdoges" not in thisset)

###Add Set items Practise ###

##add() method is being used to add items in the set but they are in unordered stage

#Approach (1)
thisset1 = {"apple","banana","cherry","grapes","mango"}
thisset1.add("oranges")
print(thisset1)

#Approach (2)
thisset2 = {"surendra","kamlesh","jagdish","rakesh","manish","mohit"}
print(len(thisset2))
thisset2.add("chandrapal")
print(len(thisset2))

##update() method is being used to add another set into the current set

#Approach 1 (Adding another set into existing set)
thisset3 = {"hemant","lokendar","surendra","jagdish","kamlesh","yash"}
thisset4 = {10,20,30,40,50,60,70,80,90,100}
thisset3.update(thisset4)
print(thisset3)
print(len(thisset3))

#Approach 2 (Adding list into existing set)
thisset5 = {"surendra","poornima","bca",25000,9460824001}
my_list = [10,20,30,40,50,60,70,80,90,100]
thisset5.update(my_list)
print(thisset5)
print(type(thisset5))

###Remove Set items

##remove() method will raise error if items were not found

#Approach 1 (Removing items from the list)
thisset6 = {"apple",'banana',"grapes","kiwi","strawberry"}
thisset6.remove("apple")
print(thisset6)
thisset6.remove("banana")
print(thisset6)

##Approach 2 (Removing items from the list which doesn;t exist)
thisset7 ={"apple",'banana',"grapes","kiwi","strawberry"}
# thisset7.remove("surendra") 
print(thisset7) ##it will give error because this item is not presented in the set

##discard() method it will not raise error if items are not found

#Approach (1)
thisset8 = {"apple","banana","grapes","strawberry","kiwi","mango"}
thisset8.discard("apple")
print(f"This the list of the item: {thisset8}")
thisset8.discard("surendra")
print(f"This is the lisf of the item: {thisset8}") 
##It will not give error either elements present in the list of not 

#Approach (2)
thisset9 = {"surendra","singh","tanwar","poornima","bca",9460824001}
print(thisset9)
thisset9.discard("surendra")
thisset9.discard("singh")
thisset9.discard("tanwar")
print(thisset9)

##pop() method to remove an item but this method will remove any random item due to nature of set because
#it is unordered

#Approach (1)
thisset10 = {"apple","banana","cherry","grapes","hotdoges","watermelon","mango"}
thisset10.pop()
print(thisset10)

#Approach (2)
thisset11 = {"apple","banana","cherry"}
thisset11.pop()
print(thisset11)

##clear() method will empties the set items

#Approach 1
thisset12 = {"apple","banana","cherry","grapes","watermelon"}
thisset12.clear()
print(thisset12)

#Approach 2
thisset13 = {"KRISHNA","surendra","KULDEEP","RONAK"}
thisset13.clear()
print(thisset13)

##del() method will remove the entire set from the code

#Approach (1)
thisset14 = {"apple","banana","cherry","hotdoges"}
del thisset14
print(thisset14) 








