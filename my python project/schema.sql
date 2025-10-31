CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_time TEXT,
    end_time TEXT
);

CREATE TABLE IF NOT EXISTS schedules (
    event_id INTEGER,
    slot INTEGER,
    FOREIGN KEY(event_id) REFERENCES events(id)
);
