# main.py
from event import Event
import db
import scheduler

def load_sample_events():
    # Or load from CSV/db
    return [
        Event("Math Class", "09:00", "10:00"),
        Event("Physics Class", "09:30", "10:30"),
        Event("Chemistry Class", "10:30", "11:30")
    ]

def main():
    db.setup_db()
    events = load_sample_events()
    for evt in events:
        db.add_event(evt)
    events = db.get_events()

    graph = scheduler.build_conflict_graph(events)
    schedule = scheduler.color_schedule(graph)
    for event, slot in schedule.items():
        print(f"{event.name}: Slot {slot}")

if __name__ == "__main__":
    main()
