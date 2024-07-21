                ## Copy a list in python which is being used to copy the entire list or clone the list ##

#Shallow copy method or normal method to clone the list 

#Approach 1
thislist = ["surendra","mukesh","jagdish","mukesh","kamlesh","manish"]
thislist1 = thislist
print(thislist1)

#Approach 2
thislist2 = ["mukesh","rakesh","kamlesh","jagdish","sukhvinder","jagvinder","komalika"]
thislist3 = thislist2 ##passing thislist2 into thislist3
thislist3[0] = "sukesh"
print(thislist2) #Both first index will be changed due to its shallow copy nature
print(thislist3) #Both first index will be changed due to its shallow copy nature

##Deep copy method to make the clone of the list not the reference

#Copy() method used to make the clone of the list

#Approach 1
thislist4 = ["kishan","khush","suresh",'jagdish',"manish"]
thislist5 = thislist4.copy()
thislist5[0] = "This is a guy"
thislist4[0] = "He is a good boy"
print(thislist4)
print(thislist5)

#Approach 2
thislist6 = ["mukesh","jagdish","kamlesh","manish","khush","surendra"]
thislist7 = thislist6.copy()
print(id(thislist6))
print(id(thislist7))

#List() method which is also used to make the clone of the list
thislist8 = ["imran",'manish',"tushar","rishab","devansh","teerth"]
thislist9 = list(thislist8)
print(id(thislist8))
print(id(thislist9))