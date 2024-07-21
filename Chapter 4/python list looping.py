#                                 ##List looping python Practise Question

#Question 1 Initialize a variable to zero and iterate through the list, adding each element to the variable.
intial_variable = 0
mylist = [10,20,30,40,50,60,70,80,90,100]
for i in mylist:
    intial_variable +=i
##loop end without any statement
print(intial_variable)

#Question 2 Intialize a variable to one and iterate through the list, multiplying each element to the variable
starting_variable = 1
my_list1 = [10,20,30,40,50,60,70,80,90,100]
for i in my_list1: #(range(0: len(my_list1)))
    starting_variable *=i
    # print(starting_variable)
##Loop end without any statement
print(starting_variable)

#Question 3 Initialize a variable to hold the first element and iterate through the list, updating the variable if a larger element is found.
bigger_list = []
smaller_list = []
my_list1 = [10, 5, 30, 40, 50, 60, 70, 80, 90, 100]

# Initialize starting_variable with the first element of the list
# starting_variable = my_list1[0]

# for i in my_list1:
#     if i >= starting_variable:
#         bigger_list.append(i)
#         print(f"Yes, it is big {i}")
#     else:
#         smaller_list.append(i)
#         print(f"No, it is not big {i}")

# # Loop ends, print the lists
# print("Bigger list:", bigger_list)
# print("Smaller list:", smaller_list)

#Question4 Intialize a variable to hold the first element and iterate through the list, updating the variabl iterate
bigger_list = []
smaller_list= []
my_list2 = [10,5,10,40,50,60,70,80,90,100]
max_value = my_list2[9]
for i in my_list2:
    if i>=max_value:
        bigger_list.append(i)
    else:
        smaller_list.append(i)
print(f"This is bigger list: {bigger_list}")
print(f"This is smaller list: {smaller_list}")


#Question 5 Comparing each items of the list with each other
bigger_value=[]
lower_value=[]
my_list3 = [10,20,30,40,50,60,80,90,100]
for list_index, list_value in enumerate(my_list3):
    for inner_value in my_list3:
        if inner_value>list_value:
            bigger_value.append(inner_value)
            # print(f"Yes this value {inner_value} is bigger then {list_value}")
        else:
            lower_value.append(inner_value)
            # print(f"No this value {inner_value} is bigger then {list_value}")
            
print(bigger_value)
print(lower_value)

#Question 6 Count of even number:
even_count_list= []
odd_count_list =[]
even_count_value = 0
odd_count_value = 0
my_list4= [15,25,14,10,20,30,58,96,52,40,25,65,75,95,85,10,30,58,30,10,45]
for i in my_list4:
    if i %2==0:
        even_count_list.append(i)
        even_count_value+=1
    else:
        if i%2 ==1:
            odd_count_list.append(i)
            odd_count_value+=1
        else:
            print("Your value is in pointing value that's why we are not able to print the loop")
##Loop ends with no expression
print("Loop have been ended we are waiting for answer")
print(f"This is even count list {even_count_list}")
print(f"This is odd count list {odd_count_list}")

#Question 7 Finding the smallest number from the list 
my_list5= [10,20,30,40,50,60,70,80,90,10,20,5,6,4,3,2,7,8,9,9.50]
smallest_no_list = []
eveno_list = []
even_no_count=0
odd_no_list = []
odd_no_count=0
biggest_no_list =[]
smallest_no = my_list5[0]
for i in my_list5:
    if smallest_no <= i:
        smallest_no_list.append(i)
        if i%2 ==0:
            eveno_list.append(i)
            even_no_count+=1
        else:
            odd_no_list.append(i)
            odd_no_count+=1
    else:
        biggest_no_list.append(i)
print("Your loop have been completed")
print(f"This all are small value in the list{smallest_no_list} ")
print(f"This all are biggest value in the list {biggest_no_list}")
print(f"This all are biggest even_no {eveno_list}")
print(f"This all are biggest odd_no {odd_no_list}")