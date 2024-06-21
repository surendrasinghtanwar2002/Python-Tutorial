#In this section we will practise each and every string methods with practical handson to make everything clear because practising the code is the best way to master anything.

# (1) In this we will practise on creating string using 'sinqle quote doubles quotes and multiline quotes

print('Surendra Singh Tanwar') #Single line quotes
print("My name is Surendra Singh Tanwar") #Double line quotes
print("""Three line quotes in this we can write anything with our own style like how are you "you have been hacked" """)


# (2) Now we will practise on string concatenation that means we will simply add two or more then two string using + operator
#So for practising we will use two method first with variable which contain string and add those string and then direct method in which we will add two string directly in print method
var1 ="Surendra"
var2 = "Singh"
var3= "Tanwar"
print(var1+var2+var3)

#Now we will directly merge the string without any variable declaration
print("Hy"+ "My"+"Name"+"is"+"Gemini"+"how"+"may"+"I"+"help"+"you")

#now we will also merge blank space in string concatenation
print("Hy"+" "+"Surendra")

# (3) String repetition:- This allow user to repeat a single string with given number of time
var4 ="Hello" *  3
print(var4)

#String repetion direct method
print("\t Hello world my name is surendra"* 2)

# (4) String indexing and slicing: Strings are like sequences where each character has its own index position, starting from 0. You can access individual characters using indexing and extract substrings using slicing:
var5 = "Surendra Singh Tanwar"
print(var5[0:5])# printing from start range to specific end range
print(var5[6])
print(var5[10]) # printing single index char value

# (5) len() method which will help out to find the length of any string
var6 = "My name is surendra"
print(len(var6)) # Output is 19 because it also calculate the extra and wide space also actual string is 16 and 3 for extra space
 
# (6) lower() method will convert entire string to lower case
var7 = "MY NAME IS surendra SINGH TANWAR"
print(var7.lower()) #It has converted entire string to lower case

# (7) upper() method will convert entire string to upper case
var8 ="my NAME is Surendra SINGH TANWAR"
print(var8.upper()) #It has converted entire string to upper case

# (8)capitalize() method which will convert first character of first word in the entire string as capital
var9 = "my name is Surendra Singh Tanwar"
print(var9.capitalize()) #It has capitalise first word first character as capital
