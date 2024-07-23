                                ## Python Set Practise Question ##

#Question 1 (create a set of your favorite fruits. Add a new fruit to the set)
fruits = {"apple","banana","cherry","grapes"}
fruits.add("watermelon")
print(fruits)

#Question 2 (Create a set of numbers from 1 to 5. Remove the number 3 from the set)
numbers = {1,2,3,4,5}
numbers.remove(3)
print(numbers)

#Question 3 (Discard a set of number from  1 to 5. Discard the number 6 from the set)
myset= {1,2,3,4,5}
myset.discard(6)
print(myset) ##Nothing will be performed if no value have been found

#Question 4 (Create a set of random numbers. Pop an element from the set and print it.)
randomnumber= {10,20,30,40,50,60,70,80,90,100}
randomnumber.pop()
print(randomnumber)

#Question 5 (Create a set of alphabets and clear the set)
alpahabet_Set = {'a','b','c','d','e','f','g','h','i'}
alpahabet_Set.clear()
print(alpahabet_Set)

#Question 6 (Given two sets {1, 2, 3} and {3, 4, 5}, find the union of these sets.)
first_Set = {1,2,3}
second_set= {3,4,5}
final_Set = first_Set.union(second_set)
print(final_Set)

#Question 7 (Given two sets {1, 2, 3} and {3, 4, 5}, find the intersection of these sets.)
third_set = {1,2,3}
fourth_Set = {3,4,5}
final_set1= third_set.intersection(fourth_Set)
print(final_set1)

#Question 8 (Given two sets {1, 2, 3} and {3, 4, 5}, find the difference between the first and the second set)
fifth_Set = {1,2,3}
sixth_Set = {3,4,5}
final_Set2 = fifth_Set.difference(sixth_Set)
print(final_Set2)

#Question 9 (Given two sets {1, 2, 3} and {3, 4, 5}, find the symmetric difference of these sets.)
seventh_set = {1, 2, 3} 
eight_set = {3, 4, 5}
final_set3 = seventh_set.symmetric_difference(eight_set)
print(final_set3)

#Question 10 (Check if the set {1, 2} is a subset of the set {1, 2, 3})
ninth_Set = {1,2,3,4,5}
tenth_set = {10,20,30,40,50,60,1,2,3,4,5}
answer = ninth_Set.issubset(tenth_set)
print(answer)

#Question 11 (Check if the set {1, 2, 3} is a superset of the set {1, 2})
eleventh_set = {1,2,3}
twelve_Set = {1,2}
result = eleventh_set.issuperset(twelve_Set)
print(result)

#Question 12 (Convert a list of integers [1, 2, 3, 1, 2, 4] to a set and print the set)
my_Set23 = {10,20,30,40,50,60,70,80,90,100}
my_list = list(my_Set23)
print(f"This is list value :{my_list} and this is type of my_list variable {type(my_list)}")

#Question 13 (Create a set of integers and find its length.)
my_Set24 = {"surendra","lalit","surendra","elements","rakesh","mohit","rohit","jack"}
print(len(my_Set24))

#Question 14 (Check if two sets {1, 2, 3} and {3, 2, 1} are equal.)
my_Set25 = {1,2,3}
my_Set26 = {3,2,1}
if my_Set25 == my_Set26:
    print("Hurray you have a common set and their items are matched")
else:
    print("Your values are not common so please recheck it again")
    
#Question 15 (Create a set of integers and make a copy of it.)
my_Set = {10,20,30,40,50,60,70,80,90,100}
new_Set = my_Set.copy()
print(new_Set)