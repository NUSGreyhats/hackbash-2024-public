from flask import Flask, request, session
from os import urandom

app = Flask(__name__)

app.secret_key = "e627168a10ff18491e7f6f916ea88a6d6ec7fcf3b34a30af"
app.config['SESSION_COOKIE_HTTPONLY'] = False

@app.route('/')
def index():
    admin_status = "admin" if session.get('admin', False) else "not admin"
    return f'''<h1>Index page</h1>
    <p>You are {admin_status}</p>
    <a href="/login">Login</a>
    <a href="/greet">Greet</a>
    <a href="/logout">Logout</a>
    '''

@app.route('/greet')
def greet():
    name = request.args.get('name')
    if name:
        return f"<h1>Hello, {name}!</h1>"
    return '''
        <form method="GET">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "omghackbashroxors":
            session['admin'] = True
            return "You are now an admin"
        return "Invalid username or password"
    return '''
        <form method="POST">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username">
            <label for="password">Password:</label>
            <input type="password" id="password" name="password">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/logout')
def logout():
    session['admin'] = False
    return "You are now logged out"

@app.route('/secret')
def secret():
    if session.get('admin', False):
        return "The secret is 42"
    return "You are not an admin"

if __name__ == "__main__":
    app.run()