import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('data/bug_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bugs 
                 (id INTEGER PRIMARY KEY, description TEXT, priority TEXT, component TEXT)''')
    conn.commit()
    conn.close()

def log_bug(description, priority, component):
    conn = sqlite3.connect('data/bug_logs.db')
    c = conn.cursor()
    c.execute("INSERT INTO bugs (description, priority, component) VALUES (?, ?, ?)", 
              (description, priority, component))
    conn.commit()
    conn.close()

def get_all_bugs():
    conn = sqlite3.connect('data/bug_logs.db')
    df = pd.read_sql_query("SELECT * FROM bugs", conn)
    conn.close()
    return df