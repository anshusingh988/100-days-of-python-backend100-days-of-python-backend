import sqlite3
import json

DB_NAME = "jobs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Jobs Table
    c.execute('''CREATE TABLE IF NOT EXISTS jobs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  description TEXT,
                  skills TEXT,
                  embedding TEXT)''')
    # Users Table (Optional for now, but good for history)
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  resume_text TEXT,
                  skills TEXT,
                  embedding TEXT)''')
    conn.commit()
    conn.close()

class Job:
    def __init__(self, title, description, skills):
        self.title = title
        self.description = description
        self.skills = skills

# Helper to save a job
def add_job(title, description, skills, embedding):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO jobs (title, description, skills, embedding) VALUES (?, ?, ?, ?)",
              (title, description, json.dumps(skills), json.dumps(embedding)))
    conn.commit()
    conn.close()

def get_all_jobs():
    """
    Fetch all jobs from the database.
    Returns a list of dictionaries with deserialized embedding.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM jobs")
    rows = c.fetchall()
    conn.close()
    
    jobs = []
    for row in rows:
        job = dict(row)
        # Deserialize JSON fields
        try:
            job['skills'] = json.loads(job['skills'])
            job['embedding'] = json.loads(job['embedding'])
        except:
            job['skills'] = []
            job['embedding'] = []
        jobs.append(job)
    return jobs
