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

#Approach 1
with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/temp_file.txt") as file_handler2:
   print(file_handler2.readline())
   print(file_handler2.readline())
   print(file_handler2.readline())
   print(file_handler2.readline())

#Approach 2 (while loop)
with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/temp_file.txt") as file_hanlder3:
  lines = file_hanlder3.readline()
  while lines:
     print(lines,end="")
     lines = file_hanlder3.readline()

#Approach 3 (for loop)
with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/temp_file.txt") as file_hanlder4:
  list_item = file_hanlder4.readline()
  for items in list_item:
     print(f"This is my name",items, end= "")

# (3) readlines(): real all the lines into a list

#Approach 1 (basic method)
with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/multiple_lines.txt") as file_handler6:
   content = file_handler6.readlines()
   print("---------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! This is new line -----------------~!!!!!!!!")
   print(type(content))

#Approach 2 (for loop)
with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/multiple_lines.txt") as file_handler5:
   list_item1= file_handler5.readlines()
   for items in list_item1:
      print(items,end="")
