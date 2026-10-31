import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

conn = sqlite3.connect("portfolio.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        link TEXT
    )
""")
conn.commit()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM projects ORDER BY id DESC")
    projects = cursor.fetchall()
    return render_template("index.html", projects=projects)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        link = request.form["link"]
        cursor.execute(
            "INSERT INTO projects (title, description, link) VALUES (?, ?, ?)",
            (title, description, link)
        )
        conn.commit()
        return redirect("/")
    return render_template("add.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run(debug=True)