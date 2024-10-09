##Importing the jinja modules 
import jinja2

##Creating the Jinja environment object
environment = jinja2.Environment()          

##Creating the template using  from string method
template = environment.from_string("Hello Mr {{name}}")

##Rendering the items
template_output = template.render(name="Surendra")

##Printing the template output
print(f"This is the output of template ------------------>{template_output}<----------------")



