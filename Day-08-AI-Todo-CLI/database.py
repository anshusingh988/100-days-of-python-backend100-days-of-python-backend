import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'todo.db')

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT DEFAULT 'Uncategorized',
            priority TEXT DEFAULT 'Medium',
            status TEXT DEFAULT 'Pending',
            parent_id INTEGER DEFAULT NULL,
            FOREIGN KEY(parent_id) REFERENCES tasks(id) ON DELETE CASCADE
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title, category='Uncategorized', priority='Medium', parent_id=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, category, priority, parent_id)
        VALUES (?, ?, ?, ?)
    ''', (title, category, priority, parent_id))
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return task_id

def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, category, priority, status, parent_id FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def complete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    cursor.execute('DELETE FROM tasks WHERE parent_id=?', (task_id,)) # delete subtasks
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
