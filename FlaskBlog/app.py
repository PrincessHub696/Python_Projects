import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

conn = sqlite3.connect("blog.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    )
""")
conn.commit()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM posts ORDER BY id DESC")
    posts = cursor.fetchall()
    return render_template("index.html", posts=posts)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        return redirect("/")
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)