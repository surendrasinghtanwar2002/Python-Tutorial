                                                                    ## Tuple unpacking ##

#Approach 1
a = ("hello","my","name","is","surendra")
(first,second,third,fourth,fifth) = a
print(first)
print(second)
print(third)
print(fourth)
print(fifth)

#Approach 2
a =("helo","my","name","is","surendra")
(first,*second)=a
print(type(first))
print(type(second))

#Heterogenous data
mixed_tuple = ("Surendra",22,9460824001,7.60,True)
print(type(mixed_tuple[0]),mixed_tuple[0])
print(type(mixed_tuple[1]),mixed_tuple[1])
print(type(mixed_tuple[2]),mixed_tuple[2])
print(type(mixed_tuple[3]),mixed_tuple[3])
print(type(mixed_tuple[4]),mixed_tuple[4])

#repetation tuple 
my_tuple = (1,2,3,4,5,6,7,8,9,10) *3
print(my_tuple)

##concatenating two tuples into one

#Approach 1
my_first_tuple = (10,20,30,40,50,60,70,80,90,100)
my_second_tuple = (110,120,130,140,150,160,170,180,190,200)
my_final_tuple = my_first_tuple+my_second_tuple
print(my_final_tuple)

#Approach 2
my_first_tuple = (10,20,30,40,50,60,70,80,90,100)
my_second_tuple = (110,120,130,140,150,160,170,180,190,200)
my_final_tuple = my_first_tuple+my_second_tuple*3
print(my_final_tuple)

#Approach 3
my_first_tuple = (10,20,30,40,50,60,70,80,90,100)
my_second_tuple = (110,120,130,140,150,160,170,180,190,200)
my_final_tuple = my_first_tuple+my_second_tuple
print(my_final_tuple)


