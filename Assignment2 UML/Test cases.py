from Artwork import Artwork
from Exhibition import Exhibition
from Visitor import Visitor
from Ticket import Ticket
from Museum import Museum
from datetime import datetime

def main():
    # Test case for adding new artwork to the museum
    artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", datetime(1503, 1, 1), "Renaissance masterpiece", "Permanent Gallery", 63)
    artwork2 = Artwork("Starry Night", "Vincent van Gogh", datetime(1889, 1, 1), "Post-Impressionist masterpiece", "Permanent Gallery", 63)
    louvre_museum = Museum()
    louvre_museum.add_artwork(artwork1)
    louvre_museum.add_artwork(artwork2)
    print("Artworks in the museum:")
    for artwork in louvre_museum.artworks:
        print(artwork)

    # Test case for opening a new exhibition
    exhibition1 = Exhibition("Impressionist Art", datetime(2024, 4, 1), "Exhibition Hall 1")
    exhibition1.add_artwork(artwork1)
    louvre_museum.open_exhibition(exhibition1)
    print("\nExhibitions in the museum:")
    for exhibition in louvre_museum.exhibitions:
        print(exhibition)

    # Test case for purchasing tickets
    visitor1 = Visitor("Ammar", 25, "123456789")
    ticket1 = Ticket("Exhibition", visitor1, artwork1)
    visitor1.purchase_ticket(ticket1)
    print("\nTickets purchased by visitors:")
    for ticket in visitor1.tickets_purchased:
        print(ticket)

    # Test case for displaying payment receipts
    total_bill = sum(ticket.calculate_final_price() for ticket in visitor1.tickets_purchased)
    print("\nTotal bill for the visitor:", total_bill)

if __name__ == "__main__":
    main()
