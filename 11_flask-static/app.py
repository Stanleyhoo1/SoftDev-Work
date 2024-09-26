# Stanley Hoo
# UWSD
# SoftDev
# K1 -- Some things Never Change
# 2024-09-25
# time spent: 0.5

# DEMO
# basics of /static folder
import random
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return serve_fixie()


@app.route("/static/foo.html")
def h():
    print("the __name__ of this module is... ")
    print(__name__)
    return str(random.random())

@app.route("/")
def serve_fixie():
    print("The __name__ of this module is...")
    print(__name__)
    return app.send_static_file('fixie.html')


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
