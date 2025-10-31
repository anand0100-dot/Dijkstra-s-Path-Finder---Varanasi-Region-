# event.py

class Event:
    def __init__(self, name, start_time=None, end_time=None, eid=None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.id = eid

    def __repr__(self):
        return f"<Event {self.name} ({self.start_time}-{self.end_time})>"
