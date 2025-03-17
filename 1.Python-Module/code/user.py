from enum import Enum
from datetime import date
class AccountStatus(Enum):
    Active = "Active"
    Closed = "Closed"
    Canceled = "Canceled"
    Blacklisted = "Blacklisted"
    NoneStatus = "None"


class Address:
    def __init__(self, street_address, city, state, zipcode, country):
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country

class Person:
    def __init__(self, name, address, email, phone):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
class Author:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name


class Account:
    def __init__(self, id, password, status, person):
        self.id = id
        self.password = password
        self.status = status
        self.person = person

    def reset_password(self,password):
        self.password=password
        return True

class Librarian(Account):
 
    def add_book_item(Book):
        # code
        print("Book added")
        return True

    def block_member(member):
        # code
        print("Member blocked")
        return True

    def unblock_member(member):
        # code
        print("Member unblocked")
        return True 
    def __init__(self,id, password,status, person):
      super().__init__( id, password,status, person)

class Member(Account):

    def __init__(self,id, password,status, person):
      super().__init__( id, password,status, person)
    def data_of_membership(self):
        return date 
    def total_books_checkedout(self):
       #code
        return True    