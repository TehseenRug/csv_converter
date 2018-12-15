from src.main.books import Books
from src.main.converter import Converter
from src.main.csv_retriever import CSVRetriever


class CSVService:

    all_books = []

    def __init__(self):
        self.csv_retriever = CSVRetriever()
        self.converter = Converter()

    def get_books_from_csv(self):
        books = Books()
        all_books_as_dtos = []

        books_from_csv = self.csv_retriever.retrieve()
        for current_book in range(0, len(books_from_csv)):
            book = self.converter.convert(books_from_csv, current_book)
            all_books_as_dtos.append(book)

        books.allBooks = all_books_as_dtos
        return books
