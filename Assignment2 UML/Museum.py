class Museum:
    def __init__(self):
        self.artworks = []
        self.exhibitions = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def open_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)