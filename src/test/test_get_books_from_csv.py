from unittest import TestCase
from unittest.mock import patch

from src.main.book import Book
from src.main.controller import *

class TestGetBooksFromCSV(TestCase):

    allBooks = []
    book1 = None
    book2 = None

    def setUp(self):
        self.book1 = Book()
        self.book2 = Book()
        self.allBooks.append(self.book1)
        self.allBooks.append(self.book2)

    @patch('src.main.csv_service.CSVService.get_books_from_csv', return_value=allBooks)
    def test_get_books_from_csv_service(self, get_books_from_csv):
        books = get_books_from_csv()
        self.assertEqual(books, self.allBooks)
        get_books_from_csv.assert_called_once_with()
