# test_library.py
import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = self.library.add_book("Test Book", "Test Author", "2023", "1234567890")

    def test_add_book(self):
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")
        self.assertEqual(self.library.books[0].author, "Test Author")
        self.assertEqual(self.library.books[0].publication_year, "2023")
        self.assertEqual(self.library.books[0].isbn, "1234567890")

    def test_remove_book(self):
        removed_book = self.library.remove_book("1234567890")
        self.assertEqual(removed_book, self.book)
        self.assertEqual(len(self.library.books), 0)

    def test_get_book(self):
        book = self.library.get_book("1234567890")
        self.assertEqual(book, self.book)
        non_existent_book = self.library.get_book("0987654321")
        self.assertIsNone(non_existent_book)

    def test_borrow_book(self):
        borrowed_book = self.library.borrow_book("1234567890")
        self.assertEqual(borrowed_book, self.book)
        self.assertTrue(borrowed_book.is_borrowed)
        
        # Try to borrow the same book again
        already_borrowed = self.library.borrow_book("1234567890")
        self.assertIsNone(already_borrowed)

    def test_return_book(self):
        self.library.borrow_book("1234567890")
        returned_book = self.library.return_book("1234567890")
        self.assertEqual(returned_book, self.book)
        self.assertFalse(returned_book.is_borrowed)
        
        # Try to return a book that's not borrowed
        not_borrowed = self.library.return_book("1234567890")
        self.assertIsNone(not_borrowed)

    def test_list_available_books(self):
        available_books = self.library.list_available_books()
        self.assertEqual(len(available_books), 1)
        self.library.borrow_book("1234567890")
        available_books = self.library.list_available_books()
        self.assertEqual(len(available_books), 0)

    def test_list_borrowed_books(self):
        borrowed_books = self.library.list_borrowed_books()
        self.assertEqual(len(borrowed_books), 0)
        self.library.borrow_book("1234567890")
        borrowed_books = self.library.list_borrowed_books()
        self.assertEqual(len(borrowed_books), 1)

if __name__ == '__main__':
    unittest.main()