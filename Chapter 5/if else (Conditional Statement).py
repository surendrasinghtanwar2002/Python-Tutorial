                        ## Python Conditional and If else Statement ##

##Equals operator to check whether both operand have same value
a = 20
b= 30
if a == b:
    print("Yes you are both similiar")
else:
    print("No you are not similiar")
    
##!= not equals to 
car_price = 250000
my_budget = 150000
if car_price != my_budget:
    print(f"Yes your car budget is not much more the {my_budget}")
else:
    print(f"The car price is {car_price} and you have budget {my_budget}")

#less then    
my_age = 25
my_father_age = 49
if my_age < my_father_age:
    print("Yes I can't Speak in front of him")
else:
    print("Yes you can speak towards him")
    
#less then equals to 
my_brother_money = 2500
my_money = 2500
if my_money <= my_brother_money:
    print(f"You both have same money and total money is{my_money+my_brother_money}")
else:
    print(f"You don't have the same money")

#Greater then equals to
my_list = [10,20,30,40,50,60,70,80,90,100]
first_value = my_list[0]
second_value = my_list[1]
if first_value >= second_value:
    print(True)
else:
    print(False)

#Greater then
my_list= [10,20,3,40,50,60,70,80,90,100]
first_value = my_list[1]
second_value = my_list[2]
if first_value > second_value:
    print("Yes you are big")
else:
    print("No you are not big")
    
##elif statement or we can say a nested if else statement
a = 33
b = 33
if a>b:
    print("Yes you are bigger")
elif a ==b:
    print("Yes you both are equals")
    
##elif statement with else statement
a = 23
b = 33
if a >= b:
    print("Yes")
else:
    print("False")

##Short hand if statement
a = 40
b = 50
if a>b: print("yes a is Greater then b")

##Short hand if else statement
print("a") if a <=b else print("B")


# This technique is known as Ternary Operators, or Conditional Expressions.
a = 20
b= 30
print("a") if a >b else print("no this Condition is also not right") if a ==b else print("Nothing is right")


##Ternary Operators
a = 40
b = 50
print("A is smaller then b") if a <= b else print("A is bigger then a") if a >=b else print("No Condition have been fullfilled")

##And Ternary Operator
a = 40
c = 30
b = 60
print("You'r statement is right") if a<=b and a>=c else print("No Condition is right")


##or Ternary Operator
first_ride = 150
second_ride = 200
third_ride = 250
my_budget = 150
print("Your ride is cheaper") if my_budget <= first_ride or my_budget <=second_ride else print("No your ride is not cheaper then the price")


##not Operator

##Approach 1
password_validation_done = False
if not password_validation_done == True:
    print(password_validation_done)
else:
    print("You are not right")

##Approach 2 
my_Age = 22
my_friend_Age = 23
if not my_Age >= my_friend_Age:
    print("Your age is bigger")
else:
    print("No my age is not bigger")
    
##nested if else:
my_Age = 22
gender = "male"
minimum_age = 18
if my_Age >= minimum_age:
    print("Yes you are above the poverty line")
    if gender == "male":
        print("Yes you are male")
    else:
        print("We only need a male candidate")
else:
    print("No your are age is not as we expect from you")

#pass statement (It is being used when we dont pass any statement in if Condition so for not getting error we use pass method to bypass the error)
a = 33
b = 200
if a <b:
    pass
