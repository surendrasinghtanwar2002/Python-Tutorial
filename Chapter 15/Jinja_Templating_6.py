from jinja2 import Environment,FileSystemLoader

Employee_Data = [
    {"Employee_Name":"Surendra Singh Tanwar","test_case":"Python Module Re","score":80},
    {"Employee_Name":"Harish Kumar","test_case":"Oops with Java","score":70},
    {"Employee_Name":"Jackson","test_case":"Kali Linux Testing","score":95},
    {"Employee_Name":"RamKrishna","test_case":"Web App Testing","score":40},
    {"Employee_Name":"Murat Singh","test_case":"React Native","score":45}
]

##Creating the environment for the jinja
environment = Environment(loader=FileSystemLoader("/Users/surendrasingh/Desktop/Python-Tutorial/Chapter 15/templates/"))

##Loading the template
template = environment.get_template("Employee_Template.txt")

##Iterating data from the list 
for employee in Employee_Data:
    data = template.render(employee)

    print(f"This is your actual data of the template------------------------>\n {data}")

