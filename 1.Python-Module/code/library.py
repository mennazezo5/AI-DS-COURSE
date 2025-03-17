
class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_address(self):
        return self.address

class LibraryCard:
    def __init__(self, card_number, barcode, issued_at, active):
        self.card_number = card_number
        self.barcode = barcode
        self.issued_at = issued_at
        self.active = active

    def is_active(self):
        return self.active
    
class BarcodeReader:
    def __init__(self, id, registered_at, active):
        self.id = id
        self.registered_at = registered_at
        self.active = active

    def is_active(self):
        return self.active