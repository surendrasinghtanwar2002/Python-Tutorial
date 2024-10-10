class Company:            ## Outer Class
    def __init__(self, name: str) -> None:
        self.name = name
        self.departments = []
        print("We are calling the outer class Company")
    
    class Department:         ## Inner Class to represent a department
        def __init__(self, department_name: str) -> None:
            self.department_name = department_name
            self.employees = []
            print(f"We are calling the inner class Department: {self.department_name}")

        def add_employee(self, employee_name: str):
            self.employees.append(employee_name)
        
        def display_employees(self):
            print(f"Employees in {self.department_name}:")
            for employee in self.employees:
                print(f" - {employee}")
    
    def add_department(self, name: str):
        new_department = self.Department(department_name=name)  ## Create an instance for the Department class
        self.departments.append(new_department)
        return new_department
    
    def display_departments(self):
        print(f"Departments in {self.name}:")
        for department in self.departments:
            print(f" - {department.department_name}")


# Creating an instance for the main class
company = Company(name="Webhack Company")

# Adding departments
it_department = company.add_department(name="IT Department")
sales_department = company.add_department(name="Sales Department")
marketing_department = company.add_department(name="Marketing Department")

# Adding employees to IT department
it_department.add_employee(employee_name="Suresh")
it_department.add_employee(employee_name="Kamlesh")
it_department.add_employee(employee_name="Jagdish")
it_department.add_employee(employee_name="Harish")

marketing_department.add_employee(employee_name="Suresh")
marketing_department.add_employee(employee_name="Kamlesh")
marketing_department.add_employee(employee_name="Jagdish")
marketing_department.add_employee(employee_name="Harish")

# Displaying departments and their employees
company.display_departments()
it_department.display_employees()
marketing_department.display_employees()  # This will show no employees since none were added
