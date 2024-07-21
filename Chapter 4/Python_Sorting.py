                                    ## Sorting in python ##

##Sorting using sort method and it sort alphanumerically which means you can sort either number and alphabet

#(1)Approach 1 sorting number into ascending to descending
thissort = [10,20,30,40,50,60,70,80,90,100]
thissort.sort()
print(thissort)

#(2)Approach 2 sorting alphabet into ascending to descending
thissort1 = ["surendra","manish","jagdish","rohit","kamlesh","chandrapal","devnash","ayush","shubanshu"]
thissort1.sort()
print(thissort1)

##sorting using sort method and reverse additional method which will allow user to sort number and alphabet
#from descending to assending

#(1)Approach 1 sorting number into descending to assending
thissort2 = [100,650,450,80,45,65,80,75,40,95,450,650,478,250,120]
thissort2.sort(reverse=True)
print(thissort2)

#(2)Approach 2 sorting alphabet into descending to assending
thissort3 = ["abhishek","bandhan","jagdish","surendra","manish","chandrapal","kamlesh","suresh","jagvinder","sukhvinder"]
thissort3.sort(reverse=True)
print(thissort3)

##Sorting in list is case insensitive sort which means it will sort wrong output most of the time
thissort4 = ["Suresh","banana","kiwi","Oranges"]
thissort4.sort()
print(thissort4) ##It will not give not proper answer because it will give first priority to capital word
thissort4.sort(key=str.lower)
print(thissort4) ##It will give insensitive result means which will give perfect answer


##reverse method in the list is used to reverse that means the last element will be the first and first element will be the last

#Approach 1
thissort5 = [10,20,30,40,50,60,70,80,90,100]
thissort5.reverse()
print(thissort5) #[100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

#Approach 2
thissort6 = [40,50,60,70,80,100,10,20,30,40,50,60,70,80,90,100]
thissort6.reverse()
print(thissort6)