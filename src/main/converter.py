from src.main.author import Author
from src.main.book import Book
from src.main.genre import Genre
from src.main.title import Title

INDEX_OF_MAIN_TITLE = 0
INDEX_OF_SUB_TITLE = 1
INDEX_OF_FIRST_NAME = 2
INDEX_OF_LAST_NAME = 3
INDEX_OF_MAIN_GENRE = 4
INDEX_OF_SUB_GENRE = 5
INDEX_OF_APPEARANCE_YEAR = 6


# noinspection PyMethodMayBeStatic
class Converter:

    def setup_genre(self, books_from_csv, book):
        genre = Genre()
        genre.mainGenre = books_from_csv[book][INDEX_OF_MAIN_GENRE]
        genre.subGenre = books_from_csv[book][INDEX_OF_SUB_GENRE]
        return genre

    def setup_author(self, books_from_csv, book):
        author = Author()
        author.firstName = books_from_csv[book][INDEX_OF_FIRST_NAME]
        author.lastName = books_from_csv[book][INDEX_OF_LAST_NAME]
        return author

    def setup_title(self, books_from_csv, book):
        title = Title()
        title.mainTitle = books_from_csv[book][INDEX_OF_MAIN_TITLE]
        title.subTitle = books_from_csv[book][INDEX_OF_SUB_TITLE]
        return title

    def convert(self, books_from_csv, book_from_csv):
        book = Book()
        book.author = self.setup_author(books_from_csv, book_from_csv)
        book.title = self.setup_title(books_from_csv, book_from_csv)
        book.genre = self.setup_genre(books_from_csv, book_from_csv)
        book.appearanceYear = books_from_csv[book_from_csv][INDEX_OF_APPEARANCE_YEAR]
        return book
