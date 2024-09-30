# Stanley Hoo, Alex Luo, Ryan Zhou
# Wild Blasters
# SoftDev
# K13 -- Template for Success
# 2024-09-30
# time spent: 0.5

from flask import Flask
app = Flask(__name__)    

import csv
import random

with open("data/occupations.csv", newline="") as csvfile:
    #creates a dictionary for every row that can be parsed through
    reader = csv.DictReader(csvfile)
    jobs = []
    percents = []
    for row in reader:
        jobs.append(row['Job Class']), percents.append(float(row['Percentage']))
        
def RandomManual():
    # find a valid percentage, subtract percents until random <=0 and we can return the corresponding jobs
    rand = random.random() * percents[-1]
    for i in range(len(percents)):
        rand -= percents[i]
        if rand <= 0:
            return jobs[i]
        
        
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

def make_table(lists):
    #html table shell
    html_table = '''
        <table class="table" border=1>
            <thead>
                _THEAD_
            </thead>
            <tbody>
                _TBODY_
            </tbody>
        </table>'''
    html_table = html_table.replace("_THEAD_", "<th>Occupations</th>")
    tbody = ""
    #using the stats shell, it replaces each of them with the pokemon's actual stats, also if there is no 2nd type it puts none
    for i in lists:
        tbody += "<tr>" + i + "</tr>\n\t</tr>\n\t"
    html_table = html_table.replace("_TBODY_", tbody[:-2])
    return html_table


def htmlOut(template):
    template = template.replace("HEADER", "<h1>Team Name: Wild Blasters - Roster: Stanley Hoo, Marco Quintero, Dua Baig</h1>\n")
    template = template.replace("TITLE", "Template for Success\n")
    body = ''
    body += "<p>Period 4</p>\n"
    body += f"<p>{RandomManual()}</p>\n"
    body += make_table(jobs)
    template = template.replace("BODY", body)
    return template    

@app.route("/")                         
def hello_world():
    print(__name__)                  
    a = htmlOut(html_website)
    print(a)
    return a

if __name__ == "__main__":
    app.debug = True
    app.run()     