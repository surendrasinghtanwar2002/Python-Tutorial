#In this section we will discuss abot the python escape characters

#If we want to add characters in existing string is illegal and it can be possible using escape character.
# THIS allow to insert any character between the string with some special characters or we can say symbol


# \n This is new line escape character used to add new line between the string
print("Hello everyone my name is Surendra \nI belong from balotra Rajasthan")

# \' This is escape character used to allow you to use double quotes when you normaly would not be allowed:
print("This is the \"Alert\" from the north zone")

print("This is Jarvis \"Your pc is being hacked\" \'A /'Please shutdown your pc")


#\r	Carriage Return This is the escape character being used to put cursor in first line
print("Hello world \rWorld")


#using sep function to specify how to seperate two or multiple values and by default space or blank space is seperator instead we can use sep function to specify a special character between the space 
print("a", 7, 8, 9,10, sep="-")

#using end function to specify that whatever we want to print before any statement print
print("Hello world", 8,9,10,sep="~" ,end=" \n009")
print("Harry bhai")