from datetime import date
from book import Book
from abc import ABC, abstractmethod
class Searchable(ABC):
    @abstractmethod
    def search_by_title(self, title: str) -> list:
        pass

    @abstractmethod
    def search_by_author(self, author: str) -> list:
        pass

    @abstractmethod
    def search_by_subject(self, subject: str) -> list:
        pass

    @abstractmethod
    def search_by_publication_date(self, date: str) -> list:
        pass

class Catalog(Searchable):
    def __init__(self,creation_date,total_books,book_titles,book_authors,book_subjects,book_publication_dates):
        self.creation_date = creation_date
        self.total_books = total_books
        self.book_titles = book_titles
        self.book_authors = book_authors
        self.book_subjects =book_subjects
        self.book_publication_dates = book_publication_dates

    def update_catalog(self):
        # Logic to update catalog
        return True
    

    def search_by_title(self, title: str) -> list:
        return [book for book in self.book_titles if title.lower() in self.book_titles]

    def search_by_author(self, author: str) -> list:

        return [book for book in self.book_authors if author.lower() in  self.book_authors ]

    def search_by_subject(self, subject: str) -> list:
        return [book for book in self.book_subjects if subject.lower() in self.book_subjects]
    def search_by_publication_date(self, date: str) -> list:
        return [book for book in self.book_publication_dates if date in self.book_publication_dates]
    
