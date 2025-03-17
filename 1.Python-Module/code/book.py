from enum import Enum

class BookFormat(Enum):
    Hardcover = "Hardcover"
    Paperback = "Paperback"
    Audiobook = "Audiobook"
    Ebook = "Ebook"
    Newspaper = "Newspaper"
    Magazine = "Magazine"
    Journal = "Journal"

class BookStatus(Enum):
    Available = "Available"
    Reserved = "Reserved"
    Loaned = "Loaned"
    Lost = "Lost"

class ReservationStatus(Enum):
    Waiting = "Waiting"
    Pending = "Pending"
    Completed = "Completed"
    Canceled = "Canceled"
    NoneStatus = "None"



class Book:
    def __init__(self, ISBN, title, subject, publisher, language, number_of_pages):
        self.ISBN = ISBN
        self.title = title
        self.subject = subject
        self.publisher = publisher
        self.language = language
        self.number_of_pages = number_of_pages

    def get_title(self):
        return self.title

class BookItem(Book):
    def __init__(self, barcode, is_reference_only, borrowed, due_date, price, format, status, date_of_purchase, publication_date):
        super().__init__(barcode, "", "", "", "", 0)  #  values
        self.barcode = barcode
        self.is_reference_only = is_reference_only
        self.borrowed = borrowed
        self.due_date = due_date
        self.price = price
        self.format = format
        self.status = status
        self.date_of_purchase = date_of_purchase
        self.publication_date = publication_date

    def checkout(self):
        if self.status == BookStatus.Available:
            self.status = BookStatus.Loaned
            return True
        return False
    

class BookReservation:
    def __init__(self, creation_date, status):
        self.creation_date = creation_date
        self.status = status

    def get_status(self):
        return self.status

    def fetch_reservation_details(self):
        return self    

class BookLending:
    def __init__(self, creation_date, due_date, return_date):
        self.creation_date = creation_date
        self.due_date = due_date
        self.return_date = return_date

    def get_return_date(self):
        return self.return_date


class Rack:
    def __init__(self,number,location_identifier):
        self.number = number  
        self.location_identifier = location_identifier
