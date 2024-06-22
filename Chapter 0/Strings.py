# In this section we will practise on various string concepts to learn string in more better way
#A string is a sequence of characters. In Python, you can create a string by enclosing text in single quotes ('), double quotes ("), or triple quotes (''' or """).


#String is started with single quotes and double quotes & they are unmuttable
#You can create strings using single quotes ('), 
# double quotes ("), or triple quotes (''' or """):


# SINGLE QUOTES STRING
singlequotestring ='Hello world'
print(singlequotestring)

#DOUBLE QUOTE STRING
doublequotesstring = "Hy surendra"
print(doublequotesstring)

#TRIPLE QUOTES STRING OR MULTI LINES
triplequotesstring= """Strings in Python are a sequence of characters, and they are one of the most commonly used data types. Python provides a 
wide range of methods "and operations for string manipulation".
 Here’s a comprehensive guide to working with strings in Python:"""
print(triplequotesstring)

#"""String various operation which are being performed on string"""

# (1)Concatenation:- Concatenate is a process of combining two or more strings into a single larger string.
FirstString ="Surendra"
SecondString = "Singh"
ThirdString = "Tanwar"
print(FirstString+SecondString+ThirdString) # In this we are adding three string at a same time.

# (2)Repetition:- String can be repeated using the * Operator in python

RepatingString = "Hello"*3
print(RepatingString)

# (3) Indexing:- Strings support indexing that means each character have their indexing value and this indexing values start from the 0 (to get a single character)
S = "HELLOW my name is surendra"
print(S[0])
print(S[1])
print(S[2])
print(S[3])
print(S[4])
print(S[5])
print(S[6]) #This indexing value is for space that means it allocate a storage to space also
print(S[7])
print(S[8])
print(S[9]) #This indexing value is for space that means it allocate a storage to space also
print(S[10])
print(S[11])
print(S[12])
print(S[13])
print(S[14]) #This indexing value is for space that means it allocate a storage to space also
print(S[15])
print(S[16])
print(S[17])
print(S[18])
print(S[19])
print(S[20])
print(S[21])
print(S[22])
print(S[23])
print(S[24])
print(S[25])


                    #String Methods: Python provide many built in function for string manipulation
#len():- The length of a string can be obtained using the len() function:
length = "Hello"
print(len(length)) #In this we have learnt that the lenght function also calculate the space or extra space and add in the length

#Lower Method:- This built function allow user to convert all character or a string to lower case and this functions skip number and special character and not throw any error
text = "SURENDRA@123"  #As we can see it will lower the character while skiping numerical and special character
x = text.lower()
print(x)

text1 = "SURENDRA SINGH TANWAR"
y = text1.lower()
print(y)

#Upper Method:- This built in function will convert all the character to upper case
text2 = "this is small heading but if you want to convert this small heading into big heading then we need to do something crazy"
z = text2.upper()
print(z) #as we can see it convert the entire string to upper case.

#Capitalize method:- This is built in function will convert the first character to Capital and rest will be same as we declare in initial stage
text3 = "surendra singh tanwar"
print(text3.capitalize()) #As we can see we can also use all this function without passing all those string to new variable

#Title method:- This is is built in function which will convert first character of each word.
text4 ="my name is surendra singh tanwar" #word means the sentence which is being written after every space
print(text4.title())

#swapcase method: In this we swaps all the existing character that means it will convert the lowercase character to uppercase and uppercase to lowercase
text5 = "mY nAME iS sURENDRA sINGH Tanwar"
print(text5.swapcase())



#Slicing method: This method is being used to find or portion of a string because each string have their indexing value and through the index value we can find their position
# which means on which index which characters stands
# For example hello its start with 0 and end with 4 so in this string e stand with 1 index so for finding that position 
# python provide a method called slicing
# To find any subsequneces from a sequence then we need only three paramter (start,stop,and step)
text6= "Hello"
print(text6[0:2]) #In this it will skip the index 2 value and give value of index 1
print(text6[0:4])
print(text6[:5]) #If forgot to give starting index value so bydefault python will allocate 0 index

text7= "Hello world How are you"
print(text7[0:8])

text9="hello"
print(len(text9), text9[0:-3])
#so basically when we denote a negative index value so it will add automatically a length function and
#calculate the actual length of a text then it will subtract the given number from the length of the text
# suppose we have hello of 5 length and i have given -3 then it will give 2 index value and output will be 0 & 1 index value only & end value should be greater then start one
text10= "Harry"
print(text10[-3:-2])
print(text10[-4:-3])
print(text10[-2:-2])
print(text10[-4:-2])
print(text10[-3:-1])

#rstrip method and this function will allow any trailing character like !@ such like that from the string from the right side and not effect on left side
text11 = "!!!!Hello!!!!!!"
print(text11.rstrip("!"))

#replace method will allow to change the existing string with new string
text12="HarryHarry"
print(text12.replace("Harry","Surendra")) #In this we have to allocate first name with new name and this will change in this specific line only not the existing variable
print(text12)

#split method this will create the normal variable into list and for that we need a space in each word in the variable theny only it will create list
text13="Harish Mohan Rohan"
print(text13.split(" "))
print(text13.split(" "))

#center method this will center any text with given parameter and we can also check the space using length function
text14="Welcome to our code"
print(len(text14))
print(len(text14.center(60)))

#count method this will find any specific word in your existing variable
text15="harry surendra harry surendra harry surendra"
print(text15.count("harry"))

#endswith() function it will check that our string is ending with specific string or value
text16="Surendra singh tanwar"
print(text16.endswith("tanwar"))

text17 = "Hello harish how are you I am fine what about you!!!!"
print(text17.endswith("!"))

text18= "Welcome to the console !!!"
print(text18.endswith("the",10,14)) # This method will basically check that the string from startind index to ending index and if it is exist then it will give us ture otherwise it will give us false

#find() method or function which will find the first word from the existing string and give starting index value no
text19 = "Welcome to hackerearth Mr Surendra Singh Tanwar"
print(text19.find("to"))

print(text19.find("tofff")) #If we check any wrong word then it will give -1 that mean the word which you are finding in the existing string is not avilable

#index() method or function which will work simliar with find function but when we give those word from existing string find return -1 and index will through error that's it
text20="Welcome Surendra to the Computer"
# print(text20.index("Tanwar"))

#isalnum() this method with check if existing string contain a-z,A-Z & 0-9 and if any special character are being used then it will throught out the error
text21="HelloworldMynameisSurendra"
print(text21.isalnum())

#If we give space between the word then it will give us false because it treat the space as special character
text22="Welcome back surendra"
print(text22.isalnum())

#isalpha() this method will check if existing string only contain a-z & A-Z no numerical, special and extra spaces 
text32= "Welcomebackhowareyou"
print(text32.isalpha())

#islower () method will check that our string is being in lower case or not and if it is lower then it will give true otherwise false
text33="welcome back surendra singh"
print(text33.islower())

#isprintable() method this will check and give us true if all the things which are given in the string are printable and if a single thing is not printable then it will through error
text34="Hello world"
print(text34.isprintable()) # this will give true because the string is printable

text35="Hy surendra \n How are you"
print(text35.isprintable()) #this will give false because \n is not printable on the terminal

# The isspace() method in Python is a string method used to check if all the characters in the string are whitespace characters. If the string contains only whitespace characters and at least one character, it returns True. Otherwise, it returns Falsetext36="  "
text36="  "
print(text36.isspace()) #give true

text37= "  s  "
print(text37.isspace()) #give false Contains non-whitespace characters

text38 = " \t\n "
print(text38.isspace()) #it will also give true because it is allocating space

#istitle() method will check each word first letter is capital then it will give true otherwise false
text39="Hello world"
print(text39.istitle()) #give true because both word first letter is capital

text40="Hy my name is Surendra"
print(text40.istitle()) #It will give false because some of the word first letter are not capital

#isupper() this method will check the entire string is in upper case or not  otherwise it will through the error
text41="HELLO MY NAME IS SURENDRA"
print(text41.isupper()) #give  true because entire string is in capital mode

text42="HY my name IS SURENDRA SINGH TANWAR"
print(text42.isupper()) #give false because  the entire string is not in capital mode 

#startwith() method will check if existing string starting with some word or character then it will give true otherwise false
text43="My name is Surendra Singh Tanwar"
print(text43.startswith("My")) #give true because our string is being started with My

text44="Hello world My name is Surendra Singh Tanwar"
print(text44.startswith("Hello",0,5)) #This will also give true because we are checking this string pare from starting 0 index to 5 index