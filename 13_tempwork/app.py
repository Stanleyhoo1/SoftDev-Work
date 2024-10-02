# Stanley Hoo
# Wild Blasters
# SoftDev
# K13 -- Template for Success
# 2024-09-30
# time spent: 0.5

from flask import Flask, render_template
app = Flask(__name__)    

import csv
import random

def read_csv(csvfile):
    with open(csvfile, newline='') as csv_file:
        header = next(csv_file)
        content = csv.reader(csv_file)
        dic = {}
        for row in content:
            percent = round(float(row[1]), 1)
            link=row[2]
            dic[row[0]] = [percent, link]

        dic.popitem()
        return dic
    
def choose_random(csvfile):
    data = read_csv(csvfile)
    jobs = [key for key in data.keys()]
    percents = [value[0] for value in data.values()]
    percents.sort()
    return ReturnRandom(jobs, percents), data
        
def ReturnRandom(jobs, percents):
# random.choices returns a list, [:-1] to ignore last row, k is returned list size
    return (random.choices(jobs[:-1], weights=percents[:-1], k=1)[0])
        
        
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

def make_table(lists, data):
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
    html_table = html_table.replace("_THEAD_", "<th>Occupations</th><th>Percent</th>")
    tbody = ""
    #using the stats shell, it replaces each of them with the pokemon's actual stats, also if there is no 2nd type it puts none
    for i in lists:
        tbody += f'<tr><td><a href={data[i][1]}>{i}</a></td><td>{data[i][0]}</td></tr>\n\t'
    html_table = html_table.replace("_TBODY_", tbody[:-2])
    return html_table


def htmlOut(template):
    template = template.replace("HEADER", "<h1>Team Name: Wild Blasters - Roster: Stanley Hoo, Marco Quintero, Dua Baig</h1>\n")
    template = template.replace("TITLE", "Template for Success\n")
    body = ''
    body += "<p>Period 4</p>\n"
    random_job, data = choose_random('data/occupations.csv')
    body += f"<p>{random_job}</p>\n"
    body += make_table([key for key in data.keys()], data)
    template = template.replace("BODY", body)
    html_file = open("templates/tablified.html", "w")
    print(template, file=html_file)
    html_file.close()
    return template    

@app.route("/wdywtbwygp")                         
def hello_world():
    print(__name__)                  
    htmlOut(html_website)
    return render_template('tablified.html')

if __name__ == "__main__":
    app.debug = True
    app.run()     