# Stanley Hoo
# 63
# SoftDev
# K09 -- Serve
# 2024-09-23
# v2 adds extra name print()

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go? 
    return "No hablo queso!"

app.run()

