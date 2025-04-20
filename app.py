from flask import Flask, request, render_template
import sqlite3

# important: create instance of Flask class
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html", route="/vulnerable_login")

# VULNERABLE LOGIN
@app.route('/vulnerable_login', methods=["GET", "POST"])

def vulnerable_login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Vulnerable to SQL Injection

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("Running query vulnerable:", query)
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"<h2>✅ Login successful! Welcome, {username}</h2>"
        else:
            return "<h2>❌ Login failed</h2>"

    return render_template("login.html", route="/vulnerable_login")

# SECURE route
@app.route('/secure_login', methods=["GET", "POST"])

def secure_login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # SECURE SQL

        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        print("Running query:", query)
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"<h2>✅ Login successful! Welcome, {username}!</h2>"
        else:
            return "<h2>❌ Login failed</h2>"

    return render_template("login.html", route="/secure_login")

if __name__ == '__main__':
    app.run(debug=True)

