                                                        ## In this method we learn the filter lenght ##

##Importing the modules
from jinja2 import Environment

##Creating the jinja environmment 
env = Environment()

##Create a template 
template = env.from_string("Hello mr {{name}} and your name has total letter:- {{name | length}}")

output = template.render(name="Surendra")

print(output)


