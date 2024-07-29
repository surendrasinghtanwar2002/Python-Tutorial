                                                ##Python Delete Files 

# ***Imp Point for deleting any file we need to import os modules for perfomring operation task on operating syste

import os


##finding the file using os module

if os.path.exists("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/ip_addresses2.txt"):
    print("Hurray we have found the bug inside your root directory")
else:
    print("Still going on")

##remove specific file from the path using os module
if os.path.exists("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/temp_folder/temp_value.txt"):
    os.remove("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/temp_folder/temp_value.txt")
    print("We have dont this")
else:
    print("We are not able to find the path of the code")

##remove specific folder from the path using os module
if os.path.exists("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/temp_folder"):
    os.rmdir("/Users/surendrasingh/Documents/Python-Tutorial/Chapter_6/temp_folder")
    print("We have removed this folder from your file structure")
else:
    print("We are not able to remove this file from the folder structure")
    

