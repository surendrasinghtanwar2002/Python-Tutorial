                                    ## __setitem__(self, key, value) Magic Method in python ##

##this method, you can control how your objects store values associated with keys, similar to how dictionaries or lists work.

class Employee:
    def __init__(self,employee_name:str,employee_age:int,employee_skills:list) -> None:
        self.name = employee_name
        self.age = employee_age
        self.skills = employee_skills
    
    def __setitem__(self,index,value):
        self.skills[index] = value
    
    def __getitem__(self,index):
        return self.skills[index]



##Creating the instance
t1 = Employee(employee_name="Surendra",employee_age=22,employee_skills=["Python","Javascript","C++","Networking","ReactNative","CCNP"])
t2 = Employee(employee_name="Jeremy",employee_age=28,employee_skills=["CCNA","CCNP","GO","TYPE_SCRIPTING","JAVASCRIPT"])
t3 = Employee(employee_name="Rony",employee_age=28,employee_skills=["Python","Javascript","C++","Networking","ReactNative","CCNP"])
t4 = Employee(employee_name="Jackson",employee_age=30,employee_skills=["CCNA","CCNP","GO","TYPE_SCRIPTING","JAVASCRIPT"])

t1[0] = "Hackerank"
print(t1[0])
