# Stanley Hoo, Leon Huang, Tahmim Hassan
# UWSD
# SoftDev
# K16 -- Take and Keep
# 2024-10-10
# Time spent: 2.5h

from flask import Flask, request, render_template, make_response, redirect, url_for
import os

app = Flask(__name__)

# Set secret key for session management
app.secret_key = os.urandom(32)

# Team Header
header = '''Team Name: UWSD
Roster: Stanley Hoo, Tahmim Hassan, Leon Huang'''

@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return render_template('response.html', username=username, greeting=f"Hello, {username}!", header=header, method_used=request.method)
    return render_template('login.html', header=header)

@app.route("/response", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        greeting = f"Hello, {username}!" if username else "Hello!"
        response = make_response(render_template('response.html', username=username, request="POST", greeting=greeting, header=header))
        response.set_cookie('username', username)
        return response
    elif request.method == 'GET':
        username = request.args.get('username')
        if username:
            greeting = f"Hello, {username}!"
            response = make_response(render_template('response.html', username=username, request="GET", greeting=greeting, header=header))
            response.set_cookie('username', username)
            return response
        return redirect(url_for('index'))

@app.route('/auth', methods=['GET'])
def auth():
    username = request.args.get('username')
    password = request.args.get('password')
    if username and password:
        greeting = f"Hello, {username}!"
        response = make_response(render_template('response.html', username=username, request="GET", greeting=greeting, header=header))
        response.set_cookie('username', username)
        return response
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('index'))
    logout_response = make_response(render_template('logout.html', header=header, username=username))
    logout_response.delete_cookie('username')
    return logout_response

if __name__ == "__main__":
    app.debug = True
    app.run()