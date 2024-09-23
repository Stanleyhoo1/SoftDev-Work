# Stanley Hoo
# UWSD
# SoftDev
# K08 -- Build the Cradle
# 2024-9-20
# time spent: 0.5

'''
DISCO:
Import flask on virtual env, run in terminal
QCC:
0. I did this before
1. Runs on local server
2. / references to home page
3. return prints that on the page
4. Can run virtual env in terminal
5. Code must be run in flask, cannot be run in Thonny
 ...
INVESTIGATIVE APPROACH:
We created an venv, installed flask, then ran app.py
'''

from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?

def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?
