# from .book import Book
from src.book import Book
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, publication_year, isbn):
        book = Book(title, author, publication_year, isbn)
        self.books.append(book)
        return book

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return book
        return None

    def get_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def borrow_book(self, isbn):
        book = self.get_book(isbn)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            return book
        return None

    def return_book(self, isbn):
        book = self.get_book(isbn)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return book
        return None

    def list_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

    def list_borrowed_books(self):
        return [book for book in self.books if book.is_borrowed]