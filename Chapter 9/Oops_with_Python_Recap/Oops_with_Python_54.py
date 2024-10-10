                            ## __delitem__(self, key) Magic Method in python ##

## this method, you can specify what happens when a user attempts to remove an item from an instance of your class ##

class Employee:
    def __init__(self,employee_name:str,employee_age:int,employee_skills:list) -> None:        
        self.name = employee_name
        self.age = employee_age
        self.skills = employee_skills
    
    def __delitem__(self,item):
        del self.skills[item]
    

##Creating the instance
t1 = Employee(employee_name="Surendra",employee_age=22,employee_skills=["Python","Javascript","C++","Networking","ReactNative","CCNP"])
t2 = Employee(employee_name="Jeremy",employee_age=28,employee_skills=["CCNA","CCNP","GO","TYPE_SCRIPTING","JAVASCRIPT"])
t3 = Employee(employee_name="Rony",employee_age=28,employee_skills=["Python","Javascript","C++","Networking","ReactNative","CCNP"])
t4 = Employee(employee_name="Jackson",employee_age=30,employee_skills=["CCNA","CCNP","GO","TYPE_SCRIPTING","JAVASCRIPT"])

del t1[0]
del t2[0]
del t3[0]
del t4[0]
print(t1.skills)
print(t2.skills)
print(t3.skills)
print(t4.skills)