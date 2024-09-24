# Stanley Hoo
# UWSD
# SoftDev
# K09 -- Serve
# 2024-9-23
# time spent: 0.5

import csv
import random
from flask import Flask

app = Flask(__name__)

template = '''
<!DOCTYPE html>
    <html lang="en">
    <meta charset="UTF-8">
    <title>Page Title</title>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <link rel="stylesheet" href="">
    <style>
    </style>
    <script src=""></script>
    <body>
        <div class="">
            <h1></h1>
            <p></p>
        </div>
    </body>
</html> 
'''


with open("occupations.csv", newline="") as csvfile:
    #creates a dictionary for every row that can be parsed through
    reader = csv.DictReader(csvfile)
    jobs = []
    percents = []
    for row in reader:
        jobs.append(row['Job Class']), percents.append(float(row['Percentage']))

def ReturnRandom():
# random.choices returns a list, [:-1] to ignore last row, k is returned list size
    return (random.choices(jobs[:-1], weights=percents[:-1], k=1)[0])

@app.route("/")   
def random_occupation():
    return ReturnRandom()

@app.route("/")  
def print_occupations():
    return jobs

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()