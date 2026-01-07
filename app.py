from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
    return "<h2>Welcome to VulnFlask</h2><a href='/login'>Login</a>"

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form['username']
        pwd = request.form['password']

        query = f"SELECT * FROM users WHERE username='{user}' AND password='{pwd}'"
        db = get_db()
        cur = db.cursor()
        result = cur.execute(query).fetchone()

        if result:
            return f"Welcome {user}"
        else:
            return "Login Failed"

    return '''
    <form method="POST">
      Username: <input name="username"><br>
      Password: <input name="password"><br>
      <input type="submit">
    </form>
    '''

@app.route("/profile")
def profile():
    uid = request.args.get("id")
    db = get_db()
    cur = db.cursor()
    user = cur.execute(f"SELECT username FROM users WHERE id={uid}").fetchone()
    return f"Profile: {user[0]}"

@app.route("/search")
def search():
    q = request.args.get("q")
    return render_template_string(f"<h3>Results for {q}</h3>")

if __name__ == "__main__":
    app.run(debug=True)