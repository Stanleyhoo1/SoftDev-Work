# Stanley Hoo
# 63
# SoftDev
# K09 -- Serve
# 2024-09-23

from flask import Flask
app = Flask(__name__)          # ... Imports Flask

@app.route("/")                # ...
def hello_world():
    print(__name__)            # ... Prints the name of the app in terminal
    return "No hablo queso!"   # ... Prints "No hable queso!"

app.run()                      # ... Runs Flask app
                
