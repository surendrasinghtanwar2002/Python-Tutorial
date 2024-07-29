                                ##Python File Handling##

##Reading file from the file

# (1) read(): Reads the entire file content.

#Approach 1
with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/temp_file.txt") as file_handler:
   entire_content = file_handler.read()
   print(entire_content)

#Approach 2
with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/temp_file.txt") as file_hanlder1:
   print(file_hanlder1.read())

# (2) realine(): read the content of file line by line
with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/temp_file.txt") as file_handler2:
   print(file_handler2.readline())
   print(file_handler2.readline())
   print(file_handler2.readline())
   print(file_handler2.readline())