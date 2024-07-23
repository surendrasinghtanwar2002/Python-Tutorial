## Important point all strings methods returns a new value. They don't change the original strings

#(1) captialize() method which convert the first character to upper case
first_char= "surendra singh tanwar"
print(first_char.capitalize()) #Output Surendra singh tanwar

second_char= "mukesh kumar solanki"
print(second_char.capitalize())#Output Mukesh kumar solanki

#(2) casefold() method will convert into lower case.
#This method is similar to the lower() method, but the casefold() method is stronger, more aggressive,
#meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.

third_char = "ELON MUSK"
print(third_char.casefold()) #output elon musk

fourth_char = "TONY STARK"
print(fourth_char.casefold()) #output tony stark

#(3) Lower() method will convert string into lower case
fifth_char = "SURENDRA SINGH TANWAR"
sixth_char = "VIKRAM SINGH TANWAR" 
print(fifth_char.lower()) #output surendra singh tanwar
print(sixth_char.lower()) #output vikram singh tanwar

#Comparing casefold() method with lower() method because they both convert string to lower case but how??
seventh_char = "MICROßOFT"
print(seventh_char.lower()) #output microßoft

eight_char = "MICROßOFT"
print(eight_char.casefold()) #output microssoft

#Lower():- Suitable for general case-insensitive comparisons within the English language.
#casefold():- Converts all characters in a string to a case-insensitive format. It is more thorough and intended to support more languages and special cases.

#(4) center() method will center the elements with given parameters such as lenght and character
ninth_char = "Surendra Singh Tanwar"
print(ninth_char.center(200,"*"))

tenth_char = " Welcome to my computer Lab "
print(tenth_char.center(120,"*"))

eleventh_char = " Surendra Singh Tanwar "
print(eleventh_char.center(150,"/"))

#(5) count() method will find the number of time a specific word or value come in the string
# We can also use this method with various parameter such as value, start position and end position

#without position
twelve_char = "My name is Surendra Singh Tanwar. His father name is Vikram Singh Tanwar. He belongs to Tanwar Family"
print(twelve_char.count("Tanwar"))

#with position
thirteen_char = "My family belongs to Tanwar Family and his family has only two young grand son one name is Surendra Singh Tanwar and second grand son name is kuldeep Singh Tanwar"
print(thirteen_char.count("Tanwar",0))

#(6) endswith() method is being used to find that the string end with specific value or not
#We can also use this methods with various parameter such as value, start position and end position

#without position
fourteen_char = "My famil is being living in balotra from past 30 Year."
fourteen_condition = fourteen_char.endswith(".")
print(fourteen_condition)
if fourteen_condition == True:
    print("Right")
else:
    print("Wrong")

#with position
fifteen_char = "Hello my name is Surendra Singh Tanwar and I am 22 year old."
print(fifteen_char.endswith(".", 0, 90)) #with indexing value of a strings

#(7) expandstabs() this method will the tab size of the strings 
sixteen_char = "My name is \tsurendra singh tanwar"
print(sixteen_char.expandtabs(40))

seventh_char = "My name is surendra \t and my hobby is develop those game which are \t very useful"
print(seventh_char.expandtabs(10))

#(8) find() this method will find specific string in the paragraph
# we can also use value and start location and end location to find that specific string 
eigteen_char = "My name is Surendra Singh Tanwar and Surendra is working like a hell to get the job in cisco"
print(eight_char.find("S", 0, 250))

#(9) index() this method is being used to find specific string index number
ninteen_char = "My name is surendra singh tanwar"
print(ninteen_char.index('s'))

#(10) format () method is being used to Formats specified values in a string
txt = "My name is {fname} and currently i am like a {fwork}".format(fname="Surendra", fwork="Hell")
print(txt)
