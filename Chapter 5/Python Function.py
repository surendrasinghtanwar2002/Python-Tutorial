                            ## Function practise in python ##

##Basic function in python

#Practise 1
def myfunction(name):
    return name.upper()
    
##calling function myfunction() and passing argument
result = myfunction("surendra")
print(result)

#Practise 2 
def mysecondfunction(myname):
    return myname.lower()

##passing argument in the function
result1= mysecondfunction("Surendra Singh Tanwar")
print(result1)

##Practise 3
def mythirdfunction(myfullname):
    return f"Hello {myfullname} Sir How may i assist you"

result2 = mythirdfunction("Surendra Singh Tanwar")
print(result2)

##Practise 4 
def addition(a,b):
    return a+b

##calling addition function and adding two values with each other
print(addition(10,20)) ##passing value and printing the result

##Practise 5 
def calculator(a,b,choice):
    if choice == 1:
        return a+b
    elif choice == 2:
        return a-b
    elif choice == 3:
        return a*b
    else:
        return None

##calling a function and passing the argument as per the choice
print(calculator(10,20,1)) ##choice 1
print(calculator(10,20,2)) ##choice 2
print(calculator(20,30,3)) ##choice 3
print(calculator(50,60,4))

##Practise 6 (Multiple argument at a single time)
# def greetinghello (*name):
#     usernamelist, choice = name ##unwrapping the tuple
#     for item,sequence in enumerate(usernamelist):
#         return sequence,item
    
# ##calling the function and passing the Multiple argument as a tuple
# userlist = ["surendra","mohit","kamlesh","rakesh","jagdish"]
# choice = int(input("Enter your choice = "))
# result3 = greetinghello(userlist,choice)
# print(result3) ##getting the result of the tupple
# print(type(result3))


##Practise 7 (Default Paramater if no argument have been declared)
def myname(name="surendra"):
    return name.upper()

##calling function and passing the argument
function_result = myname("jagdish")
print(function_result)
print(type(function_result))


##Practise 8 (Variable length argument if we dont know how many argument will passed to function then we will use *arg method)

#Approach 1
def my_user_Details(*userdetails):
    first_user,second_user,third_user = userdetails ##unwrapping the tupple
    if first_user != None and second_user != None and third_user != None:
        return f"{first_user.upper()}, {second_user.upper()}, {third_user.upper()}"
    else:
        return f"Your program have some technical issue please check it out"

##calling function and passing the Multiple argument to that function_result
first_user_details = input("Enter your first name: ")
second_user_details = input("Enter your second name: ")
third_user_details = input("Enter your third name: ")
result4 = my_user_Details(first_user_details,second_user_details,third_user_details)
print(result4)

#Approach 2
def my_user(*friends):
    for items in friends:
        print(items)
        return items
    
##calling function and passing a list as argument
my_friend_list = ["surendra","mukesh","kamlesh","jagdish","suresh","harish","khush"]
result5 = my_user(my_friend_list)

##printing the result of the function
print(result5)

##Approach 3
def myfun(arg, *args):
    for items in args:
        print(items)
        return arg, items


##calling a function and passing attributes
result6 = myfun("Hello","my name","is","surendra","singh","tanwar")
print(result6)










