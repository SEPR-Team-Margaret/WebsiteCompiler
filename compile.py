from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment
import os
import json

env = Environment()
env.loader = FileSystemLoader("source/.")

for file in os.listdir("source"):
    if file.endswith(".html"):
        if file == "asm.html":
            with open("source/asmdata.json", 'r') as d:
                asmdata = json.load(d)
            for asmnum, asm in enumerate(asmdata["data"]):
                template = env.get_template(file)
                s = template.render(asmdata=asm)
                with open("compiled/asm"+str(asmnum+1)+".html", 'w') as f:
                    f.write(s)

            
            
        else:
            template = env.get_template(file)
            s = template.render()
            with open("compiled/"+file, 'w') as f:
                f.write(s)
