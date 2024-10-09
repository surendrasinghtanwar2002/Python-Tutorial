##First Import the Jinja module
import jinja2

if __name__ == "__main__":
    ##Second create the Jinja Environment
    environment = jinja2.Environment()

    ##Create the template for jinja templating
    template = environment.from_string("Hello, {{ name }}!")

    ##Render the template with actual data for the placeholder 
    render_output = template.render(name="Surendra")

    print(render_output)

