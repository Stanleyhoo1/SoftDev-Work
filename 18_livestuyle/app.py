
    # Stanley Hoo, Leon Huang, Tahmim Hassan
    # UWSD
    # SoftDev
    # K18 -- Serving Looks
    # 2024-10-16
    # Time spent: .5h
 
from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods = ['GET', 'POST'])
def funct():
    return render_template('index.html')


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()