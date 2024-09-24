                    ## Accessing class methods from another class ##

class Employee:
    def __init__(self,employee_id,employee_name,employee_department) -> None:
        self.employee_id=employee_id
        self.employee_name = employee_name
        self.employee_department = employee_department
    
    def show_details(self):
        print("Employee id:-",self.employee_id)
        print("Employee Name:-",self.employee_name)
        print("Employee employee department:-",self.employee_department)

class changes:
    @staticmethod
    def show_brief(obj):
        obj.show_details()

t1 = Employee(employee_id=101,employee_department="bca",employee_name="Surendra")
changes.show_brief(t1)
