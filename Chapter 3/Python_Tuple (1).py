                                        ## Python Tuple ##

##Python Tuple (Chapter 1)

#(1) Creating tuple and basic practise

my_first_tuple = ("apple","banana","cherry","grapes","mango")
print(my_first_tuple)
print(type(my_first_tuple))
print(len(my_first_tuple))
print(my_first_tuple[0]) ##iterating value using the index number
print(my_first_tuple[1]) 
print(my_first_tuple[2])
print(my_first_tuple[3])
print(my_first_tuple[4])
print(my_first_tuple[0:4]) ##iterating value using the positive range
print(my_first_tuple[1:3])
print(my_first_tuple[2:3])
print(my_first_tuple[3:5])
print(my_first_tuple[-1]) ##iterating value using the negative index number
print(my_first_tuple[-2])
print(my_first_tuple[-3])
print(my_first_tuple[-4])
print(my_first_tuple[-5])
print(my_first_tuple[-5:-1]) ##iterating value using the negative range
print(my_first_tuple[-5:6])
print(my_first_tuple[-5:-2])
print(my_first_tuple[-5:-3])
print(my_first_tuple[-5:-4])

#(2) Allow duplicates value in the tuple
my_second_tuple = ("apple","banana","cherry","grapes","apple","banana","cherry")
print(my_second_tuple)
print(len(my_second_tuple))

#(3) Creating tuple with one item
my_third_tuple = ("apple",) #If we have to insert one item in the tuple so put comma otherwise it will treat as string
print(my_third_tuple)
print(type(my_third_tuple))

#(4) Tuple items can be of any datatype
my_fourth_tuple = ("apple",True,25.60,"Jamesbond","nagaro","jackson")
print(my_fourth_tuple)

#(5) Tuple() Constructor function (We can pass any iterable value inside it )

#Approach 1
my_list = [10,20,30,40,50,60,70,80,90,100,"Surendra","Harish","Praween","kamlesh","Khush","Jagdish"]
new_tuple = tuple(my_list)
print(type(my_list))
print(type(new_tuple))
print(new_tuple)
print(my_list)

#Approach 2
my_name = "Surendra"
second_tuple = tuple(my_name)
print(second_tuple)
print(type(second_tuple))

#Approach 3
third_tuple = tuple(("apple","banana","grapes","mango","watermelon"))
print(third_tuple)
print(type(third_tuple))

##Python tuple (Chapter 2)

#Access tuple items using positive index value
my_fifth_tuple = ("apple", "banana", "cherry")
print(my_fifth_tuple[0])
print(my_fifth_tuple[1])
print(my_fifth_tuple[2])

#Access tuple item using negative index value 
my_sixth_tuple = ("apple","banana",'cherry',"grapes")
print(my_sixth_tuple[-1])
print(my_sixth_tuple[-2])
print(my_sixth_tuple[-3])
print(my_sixth_tuple[-4])

#Access tuple item using ranges of index

#Approach 1
my_seventh_tuple = ("apple",'banana',"cherry","grapes")
print(my_seventh_tuple[-4:-1])
print(my_seventh_tuple[-3:-1])
print(my_seventh_tuple[-2:-1])
print(my_seventh_tuple[-1])

#Approach 2
my_eight_tuple = ("apple",'banana',"cherry","grapes")
print(my_eight_tuple[:5])
print(my_eight_tuple[:4])
print(my_eight_tuple[0:3])
print(my_eight_tuple[2:])

#Check if item in the tuple or not 
my_nine_tuple = ("apple","banana","cherry","grapes")
if "apple" in my_nine_tuple:
    print("Hurray we have found apple in the tuple")
else:
    print("We are not able to find apple in the tuple")
    

