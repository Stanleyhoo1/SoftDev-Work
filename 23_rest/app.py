# Stanley Hoo, Alex Luo
# Undecided
# SoftDev
# K23: A RESTful Journey Skyward
# 2024-11-20
# Time spent: 1

from flask import Flask, request, render_template, redirect, url_for, flash, session
import os, urllib.request, json

app = Flask(__name__)

TNPG = 'Undecided'
roster = 'Stanley Hoo, Alex Luo'

# Load API key
with open('key_nasa.txt', 'r') as file:
    key = file.read().strip()

# Home route
@app.route('/', methods=['GET'])
def home():
    # Make the API request
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key={key}'
    content = ''
    # Makes a request for the data
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())  # Decode and parse JSON data into dictionary
#     print(data)
    # Get the data and insert into the website
    for i in range(len(data['photos'])):
        content += f'<img src={data['photos'][i]['img_src']}><br>'
        content += f'<p>Mars Rover {data['photos'][i]['camera']['full_name']}</p>'
    return render_template('main.html', TNPG=TNPG, roster=roster, content=content)  

if __name__ == "__main__":
    app.debug = True
    app.run()
