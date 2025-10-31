# db.py
import sqlite3
from event import Event

DB_NAME = "event_scheduler.db"

def connect():
    return sqlite3.connect(DB_NAME)

def setup_db():
    with connect() as conn:
        with open("schema.sql") as f:
            conn.executescript(f.read())

def add_event(event: Event):
    with connect() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO events (name, start_time, end_time) VALUES (?, ?, ?)",
                    (event.name, event.start_time, event.end_time))
        event.id = cur.lastrowid
        conn.commit()
        return event.id

def get_events():
    with connect() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, start_time, end_time FROM events")
        rows = cur.fetchall()
        return [Event(name, start, end) for (id, name, start, end) in rows]
