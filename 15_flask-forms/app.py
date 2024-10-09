# Stanley Hoo, Leon Huang, Tahmim Hassan
# UWSD
# SoftDev
# K15 -- Take and Give
# 2024-10-08

from flask import Flask, render_template, request

app = Flask(__name__)    # Create Flask object

header = '''Team Name: UWSD
Roster: Stanley Hoo, Tahmim Hassan, Leon Huang'''

# Landing page
@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("***DIAG: Flask object ***")
    print(app)
    print("***DIAG: Request object ***")
    print(request)
    print("***DIAG: Request arguments ***")
    print(request.args)
    return render_template('login.html', header=header)

# Response page
@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    # Capture user input and request method
    username = request.form.get("username") if request.method == "POST" else request.args.get("username")
    method_used = request.method
    greeting = f"Hello, {username}!" if username else "Hello!"

    return render_template(
        'response.html',
        username=username,
        method_used=method_used,
        greeting=greeting,
        header=header
    )

if __name__ == "__main__":
    app.debug = True
    app.run()


