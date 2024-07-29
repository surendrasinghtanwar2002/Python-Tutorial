#                                     ## File handling in python ##
import os

# #File handling basic method and practise

# ##The open function is used to open a file and it take two arguments necesssary filename and mode
# f_hanlder = open("Lecture 1/ip_addresses.txt",mode="r") ##read mode
# print(f_hanlder)

# f_hanlder1 = open("Lecture 1/ip_addresses2.txt",mode="w") ##it file is not there it will create the file
# print(f_hanlder1)

# # f_hanlder2 = open("Lecture 1/ip_addresses4.txt",mode="x")
# # print(f_hanlder2)

# f_hanlder3 = open("Lecture 1/ip_addresses.txt",mode="a")
# print(f_hanlder3)

# ##opening a file and reading the content of it using prebuild functions or method
# f_hanlder4 = open("Lecture 1/ip_addresses.txt",mode="r")

# my_list = [ ]
# ##calling a f0or loop and printing the values inside the read mode
# for items in f_hanlder4:
#     my_list.append(items)
# ##loop over
# print("This is my new list",my_list)

##checking condition in the files
# f_handler5 = open("Lecture 1/ip_addresses.txt",mode="r")
# print(f"File name of the inserted file\ {f_handler5}")
# for name,modes in enumerate(f_handler5):
#     if "192.168.1.3" in modes:
#         print(f"This is the true condition {True}")
#         break
#     else:
#         pass

# ##printing the specific line of the file
# my_list = [ ]
# f_handler6 = open("Lecture 1/ip_addresses.txt")
# for items_value  in enumerate(f_handler6):
#     my_list.append(items_value)
# ##loop over 
# print(my_list[0:5])


# ##printing the number of lines in the python file
# f_handler7 = open("Lecture 1/ip_addresses.txt")
# counter = 0
# for items in f_handler7:
#     counter+=1
# print(f"The number of counter value is {counter}")

# if counter <=19:
#     print("Hurray")
# else:
#     print("Not hurray")

# ##readline method() 
# f_handler8 = open("Lecture 1/ip_addresses.txt")
# value1 = f_handler8.readline()
# value2 = f_handler8.readline()
# value3 = f_handler8.readline()
# value4 = f_handler8.readline()
# value5 = f_handler8.readline()
# value6 = f_handler8.readline()
# value7 = f_handler8.readline()
# value8 = f_handler8.readline()
# print(value1)
# print(value2)
# print(value3)
# print(value4)
# print(value5)
# print(value6)
# print(value7)
# print(value8)

# ##read method()
# f_handler9 = open("Lecture 1/ip_addresses.txt")
# temp = f_handler9.read(47)
# print(temp)
# # if "192.168.1.5" in temp:
# #     print("True")
# # else:
# #     print("False")


# f_handler10 = open("Lecture 1/ip_addresses.txt")
# print(f"This are multi line and you can print whatever you want here {f_handler10.readlines()}")
# f_handler10.close()





##Python File Write (using append method which will add new line at the end)

##Approach 1
f_handler11 = open("Lecture 1/ip_addresses2.txt",mode="a")
f_handler11.write("\nGood morning everyone")
f_handler11.close()

os.system("clear")
##calling the same filhere
f_handler12= open("Lecture 1/ip_addresses2.txt", mode="r")
print(f_handler12.read())


##Approach 2
file_hanlder = open("Lecture 1/Log_File.txt",mode="a")
file_hanlder.write(f"\nThis log should be printed at the last position")
file_hanlder.close()

file_hanlder_regain = open("Lecture 1/Log_File.txt",mode="r")
print(file_hanlder_regain.read())

##Python file write (using write method which will remove existing content with new content)

##Approach 1
f_handler13 = open("Lecture 1/ip_addresses2.txt",mode="w")
f_handler13.write("My self Hackerzone don't try to escap from the line")
f_handler13.close()

os.system("clear")
f_handler13_again = open("Lecture 1/ip_addresses2.txt")
print(f_handler13_again.read())

##Approach 2
f_handler14 = open("Lecture 1/Log_File.txt",mode="w")
f_handler14.write("!!!!!!!!!!!!!!!!! You have been hacked !!!!!!!!!!!!!!!!!!!!")
f_handler14.close()


f_handler14_Regain = open("Lecture 1/Log_File.txt",mode="r")
print(f_handler14_Regain.readline())

##Pthon delete file and for that we need to import os module to delete the existing file
os.remove("Lecture 1/Log_File.txt")
