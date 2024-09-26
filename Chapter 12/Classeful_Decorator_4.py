                                                                # Adding/Overriding Methods #
# Sometimes, you want to enhance or override existing methods of the class without changing its definition. This can be easily done using class decorators #

def Decorater(cls):
    class wrapper(cls):
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)

        def Employee_details(self):    
            return f"Your Employee entire details is \n Employee Name:- {self.Employee_name}\n Employee Department is {self.Employe_Department}\n Employee Salary is {self.Employee_Salary}"
    return wrapper


@Decorater
class Employee:
    def __init__(self, Employe_name: str, Employe_department: str, Employee_salary: int | float) -> None:
        self.Employee_name = Employe_name
        self.Employe_Department =Employe_department
        self.Employee_Salary = Employee_salary
    
    def Employee_details(self):
        return f"Your employee details name is {self.Employee_name} and Employee Department is {self.Employe_Department}"
    

def main():
    t1 = Employee(Employe_name="Surendra",Employee_salary=15000.255,Employe_department="Web Development")
    print(t1.Employee_details())

if __name__ == "__main__":
    main()