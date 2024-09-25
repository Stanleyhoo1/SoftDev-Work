# Stanley Hoo
# 63
# SoftDev
# K09 -- Serve
# 2024-09-23
# v1 removes print(__name__)

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

