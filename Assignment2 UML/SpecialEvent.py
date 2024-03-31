class SpecialEvent:
    def __init__(self, title, duration, location):
        self.title = title
        self.duration = duration
        self.location = location
        self.ticket_price = 0

    def set_ticket_price(self, ticket_price):
        self.ticket_price = ticket_price

    def get_ticket_price(self):
        return self.ticket_price

    def update_event_info(self, new_info):
        pass

    def change_ticket_price(self, new_price):
        self.ticket_price = new_price

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location