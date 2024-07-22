                                        ## Tuple Practise Question ##
                                        
## 1 Tuple Creation and Access ##
                                      
#Question 1
my_tuple = (10,20,30,40)
print(f"This is my tuple size: {len(my_tuple)} & This is my tuple: {my_tuple}")

#Question 2 
my_tuple_1 = ("USA","China","Russia","India","South-korea")
print(my_tuple_1[2])

#Question 3 
my_tuple_2 = (5,)
print(type(my_tuple_2))

## 2 Tuple Slicing and Indexing ##

#Question 1 
my_tuple_3 = (1,2,3,4,5,6,7,8,9,10)
my_first_slicing = my_tuple_3[0:3]
my_second_slicing = my_tuple_3[-3:-1]
my_final_slicing = my_first_slicing+my_second_slicing
print(my_final_slicing)

#Question 2
my_tuple_4 = ('a','b','c','d','e','f','g')
print(my_tuple_4[1:4])

#Question 3
my_tuple_5 = (1,2,3,4,5)
my_list = list(my_tuple_5)
my_list.reverse()
my_tuple = tuple(my_list,)
print(my_tuple)

## 3 Tuple immutability ##

#Question 1 (Approach 1)
my_tuple_6 = (1,2,3,4)
my_list = list(my_tuple_6)
my_list[1] = 10
my_tuple_7 = tuple(my_list)
print(my_tuple_7)

#Question 1 (Approach 2)

#created tuple
my_tuple_8 = (1,2,3,4)

#converting tuple into the list
my_list = []
number_temp_value = 0
for item in my_tuple_8:
    if item not in my_list:
        my_list.append(item) ##added item into the list one by one
        if 2 in my_list:
            number_temp_value = my_list.index(2)
            my_list[number_temp_value] = 20 ##item added succesfully 
        ##loop conversion over 
print(my_list)

#Question 2 (Approach 1)
my_tuple_9 = (10,20,30,40,50,60,70,80,90)

#converting tuple into the list 
my_list = []

for item in my_tuple_9:
    if item not in my_list:
        my_list.append(item)
        if 100 not in my_list:
            my_list.append(100)
##Loop get overed 
print(my_list)


## 4 Tuple Methods ##

#Question 1 (Approach 1)
my_tuple_10 = (1, 2, 2, 3, 4, 4, 4, 5)
print(my_tuple_10.count(4))

#Question 1 (Approach 2)
my_tuple_10 = (1,2,3,4,5,6,7,8,9,10)
count_variable = 0
for item in my_tuple_10:
   if item ==4:
       count_variable+=1
       
print(count_variable)

## Tuple unpacking ##

#Question 1
my_tuple_11 = ("surendra","mohan","kamlesh","suresh","jagdish","harish")
(student1,student2,student3,student4,student5, student6) = my_tuple_11
print(student1)
print(student2)
print(student3)
print(student4)
print(student5)
print(student6)
        
#Question 2 
my_dimension = (1920,1080)
(width,height) = my_dimension
print(f"Dimension of your phone is {width} + {height}")

##6. Nested Tuple

#Question 1
my_tuple_12 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(my_tuple_12[1][1])

#Question 2
my_tuple_13 = ((1,2),(3,4),(5,6))
print(my_tuple_13[0][1])
print(my_tuple_13[1][1])
print(my_tuple_13[2][1])


##7. Tuple Operations

#Question 1
first_tuple = (1,2,3)
second_tuple = (4,5,6)
final_tuple = first_tuple+second_tuple
print(final_tuple)

#Question 2
third_tuple = ('a','b','c') *3
print(third_tuple)






