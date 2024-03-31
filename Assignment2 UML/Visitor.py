class Visitor:
    def __init__(self, name, age, id_card):
        self.name = name
        self.age = age
        self.id_card = id_card
        self.tickets_purchased = []

    def purchase_ticket(self, ticket):
        self.tickets_purchased.append(ticket)

    def cancel_ticket(self, ticket):
        self.tickets_purchased.remove(ticket)

    def update_visitor_info(self, new_info):
        pass

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_id_card(self):
        return self.id_card

    def set_id_card(self, id_card):
        self.id_card = id_card