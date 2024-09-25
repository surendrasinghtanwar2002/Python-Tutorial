                                         ## __getitem__(self, key) Magic methods in python ##

#This method, you can specify how to retrieve items from your object using square bracket notation (e.g., obj[key]).

class Employee:
    def __init__(self,employee_name:str,employee_age:int,employee_skills:list) -> None:
        self.employee_name = employee_name
        self.employee_age = employee_age
        self.employee_skills = employee_skills

    def __getitem__(self,key):
        return f"{self.employee_name}:- {self.employee_skills[key]}"

##Creating the instance
t1 = Employee(employee_name="Surendra",employee_age=22,employee_skills=["Python","Javascript","C++","Networking","ReactNative","CCNP"])
t2 = Employee(employee_name="Jeremy",employee_age=28,employee_skills=["CCNA","CCNP","GO","TYPE_SCRIPTING","JAVASCRIPT"])
t3 = Employee(employee_name="Rony",employee_age=28,employee_skills=["Python","Javascript","C++","Networking","ReactNative","CCNP"])
t4 = Employee(employee_name="Jackson",employee_age=30,employee_skills=["CCNA","CCNP","GO","TYPE_SCRIPTING","JAVASCRIPT"])


print(t1[0])
print(t2[2])
print(t3[4])
print(t4[1])