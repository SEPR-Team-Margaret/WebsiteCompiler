from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment
import os

env = Environment()
env.loader = FileSystemLoader('templates/.')

for file in os.listdir("templates"):
    if file.endswith(".html"):
        template = env.get_template(file)
        s = template.render()
        with open("compiled/"+file, "w") as f:
            f.write(s)
