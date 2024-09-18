                                                    ## Built in methods class function for instance attributes ##


#(1) getattr(object_name,attribute_name)
#(2) setattr(object_name,attribute_name,new_value)
#(3) delattr(object_name,attribute_name)
#(4) hasattr(object_name,attribute_name)            ---> This will check either object has attribute if yes return True else False

class Email:
    def __init__(self,sender_name:str,receiver_name:str) -> None:
        self.sender_name = sender_name
        self.receiver_name = receiver_name

##Creating the instance or ojbect 
e1 = Email(sender_name="xyz@gmail.com",receiver_name="jackson@gmail.com")
e2 = Email(sender_name="abc@gmail.com",receiver_name="kalilinux@gmail.com")
e3 = Email(sender_name="jkl@gmail.com",receiver_name="harry@gmail.com")
e4 = Email(sender_name="jordan@gmail.com",receiver_name="helly@gmail.com")
e5 = Email(sender_name="starbucks@gmail.com",receiver_name="surendra@gmail.com")

print(f"Before changes {e1.__dict__}")

##using the getattr method to get the instance attributes variable value
print(f"Before Changes {getattr(e1,"sender_name")}")
print(f"Before Changes {getattr(e2,"sender_name")}")
print(f"Before Changes {getattr(e3,"sender_name")}")
print(f"Before Changes {getattr(e4,"sender_name")}")
print(f"Before Changes {getattr(e5,"sender_name")}")

print(getattr(e1,"receiver_name"))
print(getattr(e2,"receiver_name"))
print(getattr(e3,"receiver_name"))
print(getattr(e4,"receiver_name"))
print(getattr(e5,"receiver_name"))

##using the setattr method to set the instance attributes variable value / Manipulating the instance variable data
setattr(e1,"sender_name","moras@gmail.com")
setattr(e2,"sender_name","moras@gmail.com")
setattr(e3,"sender_name","moras@gmail.com")
setattr(e4,"sender_name","moras@gmail.com")
setattr(e5,"sender_name","moras@gmail.com")

setattr(e1,"receiver_name","surendra@gmail.com")
setattr(e2,"receiver_name","surendra@gmail.com")
setattr(e3,"receiver_name","surendra@gmail.com")
setattr(e4,"receiver_name","surendra@gmail.com")
setattr(e5,"receiver_name","surendra@gmail.com")

print(f"After Changes {getattr(e1,"sender_name")}")
print(f"After Changes {getattr(e2,"sender_name")}")
print(f"After Changes {getattr(e3,"sender_name")}")
print(f"After Changes {getattr(e4,"sender_name")}")
print(f"After Changes {getattr(e5,"sender_name")}")

print(f"After Changes {getattr(e1,"receiver_name")}")
print(f"After Changes {getattr(e2,"receiver_name")}")
print(f"After Changes {getattr(e3,"receiver_name")}")
print(f"After Changes {getattr(e4,"receiver_name")}")
print(f"After Changes {getattr(e5,"receiver_name")}")


##using the hasattr method to find the instance variable in the object and if it exist then return True else return False
print(hasattr(e1,"receiver_name"))          ##Before deleting it will give true
print(hasattr(e2,"receiver_name"))
print(hasattr(e3,"receiver_name"))
print(hasattr(e4,"receiver_name"))
print(hasattr(e5,"receiver_name"))

delattr(e1,"sender_name")                   ##Deleting the attributes from the object
delattr(e2,"sender_name")
delattr(e3,"sender_name")
delattr(e4,"sender_name")
delattr(e5,"sender_name")

delattr(e1,"receiver_name")
delattr(e2,"receiver_name")
delattr(e3,"receiver_name")
delattr(e4,"receiver_name")
delattr(e5,"receiver_name")

print(hasattr(e1,"sender_name"))        ##After deleting the attributes from the object
print(hasattr(e2,"sender_name"))
print(hasattr(e3,"sender_name"))
print(hasattr(e4,"sender_name"))
print(hasattr(e5,"sender_name"))


# setattr(e1,"sender_name","surendra@gmail.com")

print(e1.__dict__)

