import sqlite3
from datetime import datetime

# Initialize or connect to DB
def init_db():
    conn = sqlite3.connect("mood_history.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    mood TEXT,
                    song TEXT,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

# Insert record
def insert_record(mood, song):
    conn = sqlite3.connect("mood_history.db")
    c = conn.cursor()
    c.execute("INSERT INTO history (mood, song, timestamp) VALUES (?, ?, ?)",
              (mood, song, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# Fetch history
def get_history():
    conn = sqlite3.connect("mood_history.db")
    c = conn.cursor()
    c.execute("SELECT mood, song, timestamp FROM history ORDER BY timestamp DESC")
    data = c.fetchall()
    conn.close()
    return data

# Clear history
def clear_history():
    conn = sqlite3.connect("mood_history.db")
    c = conn.cursor()
    c.execute("DELETE FROM history")
    conn.commit()
    conn.close()
