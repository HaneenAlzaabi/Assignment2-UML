class Exhibition:
    def __init__(self, title, start_date, location):
        self.title = title
        self.start_date = start_date
        self.location = location
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def remove_artwork_from_exhibition(self, artwork):
        self.artworks_displayed.remove(artwork)

    def extend_exhibition_duration(self, new_duration):
        self.duration = new_duration

    def change_exhibition_location(self, new_location):
        self.location = new_location

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