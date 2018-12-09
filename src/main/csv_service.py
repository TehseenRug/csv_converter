from src.main.author import Author
from src.main.book import Book
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
    all_books_as_dtos = []
    def __init__(self):
        self.csv_retriever = CSVRetriever()

    def get_books_from_csv(self):

        books_from_csv = self.csv_retriever.retrieve()
        for current_book in range (0, len(books_from_csv)):
            book = Book()
            title = Title()
            author = Author()
            genre = Genre()
            title.mainTitle = books_from_csv[current_book][INDEX_OF_MAIN_TITLE]
            title.subTitle = books_from_csv[current_book][INDEX_OF_SUB_TITLE]
            author.firstName = books_from_csv[current_book][INDEX_OF_FIRST_NAME]
            author.lastName = books_from_csv[current_book][INDEX_OF_LAST_NAME]
            genre.mainGenre = books_from_csv[current_book][INDEX_OF_MAIN_GENRE]
            genre.subGenre = books_from_csv[current_book][INDEX_OF_SUB_GENRE]
            book.author = author
            book.title = title
            book.genre = genre
            book.appearanceYear = books_from_csv[current_book][INDEX_OF_APPEARANCE_YEAR]
            print(book)
            self.all_books_as_dtos.append(book)
        return self.all_books_as_dtos
