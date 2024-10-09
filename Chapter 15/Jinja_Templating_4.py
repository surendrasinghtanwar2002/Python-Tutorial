##Importing the Jinja Module
from jinja2 import Environment,FileSystemLoader

##Data for the message 
details = [
    {"greeting":"Morning","fullname":"Surendra Singh Tanwar","college_name":"Poornima University"},
    {"greeting":"Evening","fullname":"Harish Kumar","college_name":"Jecrc University"},
    {"greeting":"Night","fullname":"Jagdish Kumar","college_name":"Shubodh University"}
]

##Load the template path for jinja tempalting 
jinja_evironment = Environment(loader=FileSystemLoader("/Users/surendrasingh/Desktop/Python-Tutorial/Chapter 15/templates/"))

##There can be various template in single folder so we need to specify which template we have to used 
template = jinja_evironment.get_template("message.txt")

##Render the items from the details
for detail in details:
    filename = f"message_{detail['fullname'].lower()}.txt"              ##Create the file path
    content = template.render(detail)


    ##Creating file for each message
    with open(filename,"w",encoding="utf-8") as message:
        message.write(content)
        print(f"Your file have been created {filename}")