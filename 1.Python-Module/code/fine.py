class Fine:
    def __init__(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

class FineTransaction(Fine):
    def __init__(self, creation_date, amount):
        super().__init__(amount)
        self.creation_date = creation_date

    def initial_transaction(self):
        # Logic to initiate transaction
        return True

class CashTransaction(FineTransaction):
    def __init__(self, creation_date, amount, cash_tendered):
        super().__init__(creation_date, amount)
        self.cash_tendered = cash_tendered

class CheckTransaction(FineTransaction):
    def __init__(self, creation_date, amount, bank_name, check_number):
        super().__init__(creation_date, amount)
        self.bank_name = bank_name
        self.check_number = check_number

class CreditCardTransaction(FineTransaction):
    def __init__(self, creation_date, amount, name_on_card):
        super().__init__(creation_date, amount)
        self.name_on_card = name_on_card


