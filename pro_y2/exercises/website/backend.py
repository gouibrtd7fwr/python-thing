from flask import Flask, render_template, url_for, request, session, redirect
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "abc123zyx"

database = Path(__file__).resolve().with_name("shop.db")

def getConnection():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn

def makeTables():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        username TEXT,
        name TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(id)
        FOREIGN KEY (product_id) REFERENCES product(id)
    )
    """)

def insertSampleData():
    conn = getConnection()
    cursor = conn.cursor()
    list_user = [
        ('maria3311@gmail.com', 'Maria22', '8883311'),
        ('johnjacks777@yahoo.com', 'John Jacks', '@john1470'),
        ('lora120392@gmail.com', 'Lora Kevin', 'lorlikesmusic!')
    ]

    list_product = [
        ("Snippet Sharing", 5),
        ("Automatic Error Detector", 1),
        ("Feather Code", 0)
    ]

    cursor.executemany("""
        INSERT INTO user (username, name, password)
        VALUES (?,?,?)
        """, list_user)

    cursor.executemany("""
        INSERT INTO product (name, price)
        VALUES (?,?)
        """, list_product)

    conn.commit()
    conn.close()

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username_demo = request.form["username"]
        password_demo = request.form["password"]

        conn = getConnection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM user
        WHERE username = ? AND password = ?
        """, (username_demo, password_demo))

        user = cursor.fetchone()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            session["name"] = user["name"]
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    makeTables()
    insertSampleData()
    app.run(debug=True)

