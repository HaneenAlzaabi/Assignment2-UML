class Artwork:
    def __init__(self, title, artist, date_of_creation, significance, location, ticket_price):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.significance = significance
        self.location = location
        self.ticket_price = ticket_price

    def add_artwork(self, artwork):
        # Add artwork to the collection
        pass

    def remove_artwork(self, artwork):
        # Remove artwork from the collection
        pass

    def update_artwork_info(self, artwork, new_info):
        # Update information of an existing artwork
        pass

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def get_date_of_creation(self):
        return self.date_of_creation

    def set_date_of_creation(self, date_of_creation):
        self.date_of_creation = date_of_creation

    def get_historical_significance(self):
        return self.historical_significance

    def set_historical_significance(self, historical_significance):
        self.historical_significance = historical_significance

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location