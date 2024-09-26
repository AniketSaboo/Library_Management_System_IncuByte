class Book:
    def __init__(self, title, author, publication_year, isbn):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year}) (ISBN: {self.isbn})"

    def __repr__(self):
        return self.__str__()