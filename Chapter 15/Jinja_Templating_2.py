                                                    ##This is right message and we will use the template for sending the message to everyone

#Import the jinja module
from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python_Challenge"

students = [
    {"name":"Surendra", "score":80},
    {"name":"Jackson", "score":70}
]

##this is the actual path of the templates
environment = Environment(loader=FileSystemLoader("/Users/surendrasingh/Desktop/Python-Tutorial/Chapter 15/templates/"))

##There can be various template in the single folder so speciying which template file should be used for that 
template = environment.get_template("message.txt")

for student in students:
    filename = f"message_{student['name'].lower()}.txt"
    content = template.render(
        student,
        max_score = max_score,
        test_name = test_name
    )

    ##Creating the file for the each message
    with open(filename,"w",encoding="utf-8") as message:
        message.write(content)
        print(f"Wrote the file {filename}")