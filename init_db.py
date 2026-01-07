import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

cur.execute("INSERT INTO users VALUES (1,'admin','admin123')")
cur.execute("INSERT INTO users VALUES (2,'hari','password')")

conn.commit()
conn.close()
