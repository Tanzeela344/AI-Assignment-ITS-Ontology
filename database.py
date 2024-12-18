import sqlite3

def initialize_db():
    conn = sqlite3.connect('progress.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        shape TEXT,
        score INTEGER
    )
    """)
    conn.commit()
    conn.close()

def update_progress(name, shape, score):
    conn = sqlite3.connect('progress.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO progress (name, shape, score) VALUES (?, ?, ?)", (name, shape, score))
    conn.commit()
    conn.close()

def fetch_progress(name):
    conn = sqlite3.connect('progress.db')
    cursor = conn.cursor()
    cursor.execute("SELECT shape, score FROM progress WHERE name = ?", (name,))
    rows = cursor.fetchall()
    conn.close()
    return rows
