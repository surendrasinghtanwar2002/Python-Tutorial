                                ##Python File Handling##

 ## Basic File handling method ##

#Open() method to open the file and read method to print entire content in the file

#Approach 1
file_handler = open("Chapter_6/File_Handling_Files/ip_Adddress.txt") 
print(file_handler.read())
file_handler.close() ##After doing it any work we need to close the file because it is in buffer stage so we need to manually push the file from buffer stage to harddisk


#Approach 2
with open("Chapter_6/File_Handling_Files/ip_Adddress.txt") as file_handler1:
    print(f"This is the new file handler",file_handler1.read()) ##we don;t to close the file it will automatically close the file and push data directly from buffer memory to original hardisk


#open() method modes such as read,write,append,binary 

#Approach 1 (Read mode) if don't specify read mode bydefault it will take the read mode itself
with open("Chapter_6/File_Handling_Files/ip_Adddress.txt") as file_hanlder2:
    print(f"This is new file which are being added {file_hanlder2.read()}")

#Approach 2 (write mode) (Prexisting files) if file is not existed it will create and if file exist it will truncate the original file into new file

with open("Chapter_6/File_Handling_Files/ip_Adddress.txt",mode="w+") as file_hanlder3:
    file_hanlder3.write("This file is being corrupted")

file_hanlder4 = open("Chapter_6/File_Handling_Files/ip_Adddress.txt")
print(file_hanlder4.read())

##Approach 3 (write mode) (File does not exist in this case)
with open("Chapter_6/File_Handling_Files/ios_logs.txt", mode="w") as file_hanlder4:
    file_hanlder4.write("You have been hacked don;t try to call the cops")
## at this stage it will create a new file and push data from buffer to physical location

with open("Chapter_6/File_Handling_Files/ios_logs.txt", mode="r") as file_hanlder4_return:
    print(file_hanlder4_return.read())