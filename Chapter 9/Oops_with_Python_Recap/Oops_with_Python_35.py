class Company:
    def __init__(self,Company_name:str) -> None:
        self.Company_Name = Company_name
        print("Outer Class Called 'Company' ")
    ##Inner Class
    class Department:
        def __init__(self,Department_name:str) -> None:
            self.name = Department_name
            self.employees = []
            print("Inner Class Called 'Inner' ")
        
        def add_employee(self,employee_name:str):
            self.employees.append(employee_name)
        
        def display_employeee(self):
            for employee in self.employees:
                print(employee)


##Create the outer class instance
c1 = Company(Company_name="Hackerrank")

##Iner Class instance
c1_inner = c1.Department(Department_name="Computer Science")

##Inner Class instance or object methods 
c1_inner.add_employee(employee_name="Rakesh")
c1_inner.add_employee(employee_name="Jagdish")
c1_inner.add_employee(employee_name="Suresh")
c1_inner.add_employee(employee_name="Kamlesh")
c1_inner.add_employee(employee_name="Jackson")
c1_inner.add_employee(employee_name="Emily")
c1_inner.add_employee(employee_name="Surendra")


print("")
c1_inner.display_employeee()



