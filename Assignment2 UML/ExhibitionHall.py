class ExhibitionHall:
    def __init__(self, capacity):
        self.capacity = capacity
        self.events_scheduled = []

    def schedule_event(self, event):
        self.events_scheduled.append(event)

    def cancel_event(self, event):
        self.events_scheduled.remove(event)

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity