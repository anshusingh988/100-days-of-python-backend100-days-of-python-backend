import sqlite3

DB_NAME = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        category TEXT,
        priority TEXT,
        status TEXT DEFAULT 'Pending',
        parent_id INTEGER
    )
    """)

    conn.commit()
    conn.close()

def add_task(title, category="General", priority="Medium", parent_id=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, category, priority, parent_id) VALUES (?, ?, ?, ?)",
        (title, category, priority, parent_id)
    )

    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return task_id

def get_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def complete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))

    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    conn.commit()
    conn.close()