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

# Home route
@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        # redirects to response.html
        return render_template('response.html', username=username, greeting=f"Hello, {username}!", header=header, method_used=request.method)
    # Redirects to login.html
    return render_template('login.html', header=header)

# Response route
@app.route("/response", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Gets username if username
        username = request.form['username']
        # Sets greeting
        greeting = f"Hello, {username}!" if username else "Hello!"
        response = make_response(render_template('response.html', username=username, method_used="POST", greeting=greeting, header=header))
        # Username in session
        response.set_cookie('username', username)
        return response
    elif request.method == 'GET':
        username = request.args.get('username')
        if username:
            greeting = f"Hello, {username}!"
            response = make_response(render_template('response.html', username=username, method_used="GET", greeting=greeting, header=header))
            response.set_cookie('username', username)
            return response
        # Returns the route corresponding to the index function
        return redirect(url_for('index'))

# Auth route to authenticate password and username
@app.route('/auth', methods=['GET', 'POST'])
def auth():
    username = request.args.get('username')
    password = request.args.get('password')
    # checks if there is both a username and password
    if username and password:
        greeting = f"Hello, {username}!"
        response = make_response(render_template('response.html', username=username, method_used=request.method, greeting=greeting, header=header))
        response.set_cookie('username', username)
        return response
    # Returns the route corresponding to the index function
    return redirect(url_for('index'))

# Logs out
@app.route('/logout')
def logout():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('index'))
    logout_response = make_response(render_template('logout.html', header=header, username=username))
    logout_response.delete_cookie('username')
    # Redirects to logout page
    return logout_response

if __name__ == "__main__":
    app.debug = True
    app.run()