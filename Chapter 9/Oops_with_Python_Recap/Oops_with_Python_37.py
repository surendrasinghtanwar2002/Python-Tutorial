class Company:
    def __init__(self, Companyname: str) -> None:
        self.Company_name = Companyname
        self.departments = []  # Renamed to 'departments' for clarity
        print("Outer Class Called")

    # Inner class for the department
    class Department:
        def __init__(self, Department_name: str) -> None:
            self.Department_name = Department_name
            self.employees = []  # Renamed to 'employees' for clarity

        def add_employee(self, employee_name: str):
            self.employees.append(employee_name)

        def display_employee(self):
            print(f"Employees in {self.Department_name}:")
            for i in self.employees:
                print(f"----->{i}")

    def add_department(self, department_name: str):
        new_department = self.Department(Department_name=department_name)
        self.departments.append(new_department)  # Appending the department object
        return new_department

    def display_departments(self):
        print(f"Departments in {self.Company_name}:")
        for department in self.departments:
             print(f"----->{department}")


# Creating the instance
company1 = Company(Companyname="Hacktheworld")

# Adding departments
it_department = company1.add_department(department_name="IT Department")
sales_department = company1.add_department(department_name="Sales Department")
marketing_department = company1.add_department(department_name="Marketing Department")

# Adding employees to IT Department
it_department.add_employee("Surendra")
it_department.add_employee("Jame")
it_department.add_employee("Remini")
it_department.add_employee("Jack")

# Adding employees to Sales Department
sales_department.add_employee("Emily")
sales_department.add_employee("Harry")
sales_department.add_employee("Rosly")

# Adding employees to Marketing Department
marketing_department.add_employee("Kevin")
marketing_department.add_employee("Ben")
marketing_department.add_employee("Jolly")

# Displaying departments
company1.display_departments()

# Displaying employees in each department
sales_department.display_employee()
marketing_department.display_employee()
it_department.display_employee()
                            