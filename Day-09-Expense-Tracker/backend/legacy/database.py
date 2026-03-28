import sqlite3

def connect():
    return sqlite3.connect("data.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        type TEXT,
        amount REAL,
        category TEXT,
        date TEXT
    )
    """)
    conn.commit()
    conn.close()