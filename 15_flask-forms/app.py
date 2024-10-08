# Stanley Hoo, Leon Huang, Tahmim Hassan
# UWSD
# SoftDev
# K15 -- Take and Give
# 2024-10-8
# time spent: 0.5

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


html_website = '''
<!DOCTYPE html>
    <head>
        <title>
            TITLE
        </title>
        <style>
        STYLE
        </style>
        HEADER
    </head>
    <body>
        BODY
    </body>
</html>'''

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
#    print("***DIAG: request.args['username']  ***")
#    print(request.args['username'])
#    print("***DIAG: request.headers ***")
#    print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
#     print("\n\n\n")
#     print("***DIAG: this Flask obj ***")
#     print(app)
    print("***DIAG: request obj ***")
#     print(request)
#     print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])
#     print("***DIAG: request.headers ***")
#     print(request.headers)
    return "Waaaa hooo HAAAH"  #response to a form submission

def htmlOut(template):
    template = template.replace("HEADER", "<h1></h1>\n")
    template = template.replace("TITLE", "Template for Success\n")
    body = ''
    body += "<p>Period 4</p>\n"
    random_job, data = choose_random('data/occupations.csv')
    body += f"<p>{random_job}</p>\n"
    body += make_table([key for key in data.keys()], data)
    template = template.replace("BODY", body)
    html_file = open("templates/response.html", "w")
    print(template, file=html_file)
    html_file.close()
    return template

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

