# In this section we will practise on various string concepts to learn string in more better way
#A string is a sequence of characters. In Python, you can create a string by enclosing text in single quotes ('), double quotes ("), or triple quotes (''' or """).


#String is started with single quotes and double quotes
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
#Length:- The length of a string can be obtained using the len() function:
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


