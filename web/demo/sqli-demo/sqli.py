from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY,
             username TEXT NOT NULL,
             password TEXT NOT NULL
             )''')
c.execute("INSERT INTO users (username, password) VALUES ('admin', 'l33tpassword')")
c.execute("INSERT INTO users (username, password) VALUES ('johnnyjohnny', 'yespapa')")
conn.commit()
conn.close()

@app.route('/')
def index():
    return """
    <body>
        <h2>Login</h2>
        <form method="post" action="/login">
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username"><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
    """

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    c.execute(query)
    user = c.fetchone()
    conn.close()

    if user:
        return f"Welcome {user[1]}!"
    else:
        return "Invalid credentials."

if __name__ == '__main__':
    app.run()
