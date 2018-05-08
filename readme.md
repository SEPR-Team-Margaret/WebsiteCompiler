# Website Compiler for SEPR-Team-Margaret

## How to Use

### Compilcation
Get Python

Install jinja 2 `python -m pip install jinja2`

Run compile.py

### Modification of templates
The compiler uses the [jinja](http://jinja.pocoo.org/docs/2.9/) templating system

Edit pages in the templates directory

To edit the assessment pages, edit the asmdata.json file in the templates directory.

```
{"data":[
  [
    {"sectiontitle":"",
     "sectiondata":[
        {"title":"", "icon":"","date":"", "link":""}
        // Add multiple items under to one section
    ]}
    // Add multiple sections to one page
  ]
  // Add multiple pages
]}
```

Commit the output files from the 'compiled' directory to the github.io repo
