                                                                        ## In this section we will create a seperate jinja template and put the condition for generating the message ##

##Importing the Jinja Module
from jinja2 import Environment,FileSystemLoader


##Details
student_details = [
    {"Student_Name":"Surendra Sing Tanwar","Mobile_No":558181891,"Score":80},
    {"Student_Name":"Jackson","Mobile_No":123456789,"Score":89},
    {"Student_Name":"Jeremy","Mobile_No":7987891651,"Score":65},
    {"Student_Name":"Kevin","Mobile_No":61151817282,"Score":95},
    {"Student_Name":"Olly","Mobile_No":73213132156156,"Score":99},
]

##Load the template 
jinja_environment = Environment(loader=FileSystemLoader("/Users/surendrasingh/Desktop/Python-Tutorial/Chapter 15/templates/"))

##Loading the tempalte from the folder mentioned above
template = jinja_environment.get_template("student_template.txt")

##Iterate each and every line from the loop
for student in student_details:
    file_name = f"Student_{student['Student_Name']}.txt"            ##Specifying the file
    data = template.render(student)        ##Rendering the items 

    ##Creating file for specific data
    with open(file_name,"w",encoding="utf-8") as message:
        message.write(data)

        print(f"File Wrote {file_name}")


