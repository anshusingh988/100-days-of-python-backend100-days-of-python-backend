import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "expense_tracker.db")

def connect():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = connect()
    cursor = conn.cursor()
    
    # Unified transactions table for professional analytics
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL,
        type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL,
        description TEXT
    )
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
