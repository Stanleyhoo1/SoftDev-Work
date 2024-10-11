# Stanley Hoo, Leon Huang, Tahmim Hassan
# UWSD
# SoftDev
# K16 -- Take and Keep
# 2024-10-10
# Time spent: 1.5h

from flask import Flask, request, render_template, redirect, url_for, flash, session
import os


app = Flask(__name__)

secret_key = os.urandom(32)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

header = '''Team Name: UWSD
Roster: Stanley Hoo, Tahmim Hassan, Leon Huang'''

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
#     return 'You are not logged in'
    return render_template('login.html', header=header)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        print(request.cookies.get('username'), username)
        session['username'] = request.form['username']
        return redirect(url_for('index'))
#         if password==app.secret_key:
#             flash('Login successful!', 'success')
#             session['username'] = request.form['username']
#             password = request.form['password']
#             return redirect(url_for('/'))
#         else:
#             flash('Incorrect username or password', 'success')
    else:
        return render_template('login.html', header=header)

@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    
    print(request.cookies.get('username'), 'username')
    session['username'] = request.form['username']
    if 'username' in session:
        message = f'Logged in as {session["username"]}'
    else:
        message = 'You are not logged in'
    username = request.args['username']
    method_used = request.method
    greeting = f"Hello, {username}!" if username else "Hello!"
    greeting += " " + message
    return render_template(
        'response.html',
        username=username,
        method_used=method_used,
        greeting=greeting,
        header=header
    )


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    username = request.args['username']
    session.pop('username', None)
    return render_template('logout.html', header=header, username=username)

if __name__ == "__main__":
    app.debug = True
    app.run()