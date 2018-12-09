from src.main.author import Author
from src.main.book import Book
from src.main.books import Books
from src.main.csv_retriever import CSVRetriever
from src.main.genre import Genre
from src.main.title import Title


INDEX_OF_MAIN_TITLE = 0
INDEX_OF_SUB_TITLE = 1
INDEX_OF_FIRST_NAME = 2
INDEX_OF_LAST_NAME = 3
INDEX_OF_MAIN_GENRE = 4
INDEX_OF_SUB_GENRE = 5
INDEX_OF_APPEARANCE_YEAR = 6


class CSVService:

    all_books = []

    def __init__(self):
        self.csv_retriever = CSVRetriever()

    def get_books_from_csv(self):
        books = Books()
        all_books_as_dtos = []

        books_from_csv = self.csv_retriever.retrieve()
        for current_book in range(0, len(books_from_csv)):
            book = self.setup_book(books_from_csv, current_book)
            all_books_as_dtos.append(book)

        books.allBooks = all_books_as_dtos
        return books

    def setup_book(self, books_from_csv, current_book):
        book = Book()
        book.author = self.setup_author(books_from_csv, current_book)
        book.title = self.setup_title(books_from_csv, current_book)
        book.genre = self.setup_genre(books_from_csv, current_book)
        book.appearanceYear = books_from_csv[current_book][INDEX_OF_APPEARANCE_YEAR]
        return book

    def setup_genre(self, books_from_csv, current_book):
        genre = Genre()
        genre.mainGenre = books_from_csv[current_book][INDEX_OF_MAIN_GENRE]
        genre.subGenre = books_from_csv[current_book][INDEX_OF_SUB_GENRE]
        return genre

    def setup_author(self, books_from_csv, current_book):
        author = Author()
        author.firstName = books_from_csv[current_book][INDEX_OF_FIRST_NAME]
        author.lastName = books_from_csv[current_book][INDEX_OF_LAST_NAME]
        return author

    def setup_title(self, books_from_csv, current_book):
        title = Title()
        title.mainTitle = books_from_csv[current_book][INDEX_OF_MAIN_TITLE]
        title.subTitle = books_from_csv[current_book][INDEX_OF_SUB_TITLE]
        return title
