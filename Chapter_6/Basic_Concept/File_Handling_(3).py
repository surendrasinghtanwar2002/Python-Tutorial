                                ##Python File Handling##

##Python writing method which is used to write 

#(1) write(): Writes a string to the file. If the file is opened in 'w' mode, it will overwrite the existing content. 

#Approach 1 (New file which doesn;t exist and add one line) 
with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/mobile_logs.txt",mode="w") as file_hanlder:
    file_hanlder.write("Hey you have been hacked don;t try to move")

with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/ios_logs.txt") as file_hanlder2:
    content = file_hanlder2.read()
    print(type(content),content)

#Approach 2 (Existing file and replacing new content )
with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/mobile_logs.txt",mode="w") as file_hanlder_1:
    file_hanlder_1.write("System hijacked")

with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/mobile_logs.txt",mode="r") as file_hanlder_1_return:
    print(file_hanlder_1_return.read())
    print(file_hanlder_1_return.read())
    print(file_hanlder_1_return.read())

#(2) writeline(): Writes a list of strings to the file.

#Approach 1 (New files which does not exist and add multiple line)
with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/mobile_logs1.txt",mode="w") as file_hanlder_4:
    new_content = ["hacked","hacked1","hacked2","hacked3","hacked4","hacked5"]
    file_hanlder_4.writelines(new_content)

with open("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/File_Handling_Files/mobile_logs1.txt",mode="r") as file_hanlder_2_return:
    print(file_hanlder_2_return.readlines())
    



mylist = [10,20,30,40,50,60,70]
help(mylist.append)