                                                            ## In this module we learn the filter lower ##

##Importing the module
from jinja2 import Environment

##Create the environment object
env = Environment()

##Use the method of env
template = env.from_string("Hello my name is {{name | lower}}")

##render the element to the template 
result = template.render(name="Surendra")

##printing the result of the template
print(f"This is your result of the template -------------> {result} <--------------------------")
