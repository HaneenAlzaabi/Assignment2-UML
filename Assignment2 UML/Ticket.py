class Ticket:
    def __init__(self, ticket_type, visitor=None, artwork=None, event=None):
        self.ticket_type = ticket_type
        self.visitor = visitor
        self.artwork = artwork
        self.event = event
        self.price = 0

    def calculate_price(self):
        if self.ticket_type == "Special Event":
            self.price = self.event.get_ticket_price()
        else:
            if self.visitor.age < 18 or self.visitor.age >= 60:
                self.price = 0
            elif self.ticket_type == "Group":
                self.price = 0.5 * self.artwork.ticket_price
            else:
                self.price = self.artwork.ticket_price

        return self.price

    def calculate_final_price(self):
        return self.calculate_price() * 1.05