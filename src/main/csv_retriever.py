import pandas as pd


class CSVRetriever:

    books_from_csv = []
    bookAttributes = ['MainTitle', 'SubTitle', 'FirstName', 'LastName', 'MainGenre', 'SubGenre', 'AppearanceYear']

    def retrieve(self):
        data_frame = pd.read_csv('../resources/books.csv')
        count_row = data_frame.shape[0]
        data_of_given_row = []

        self.handle_all_rows(count_row, data_frame, data_of_given_row)
        return self.books_from_csv

    def handle_all_rows(self, count_row, data_frame, data_of_given_row):
        for current_row in range(0, count_row):
            self.retrieve_book_in_row(current_row, data_frame, data_of_given_row)
            data_of_given_row = []

    def retrieve_book_in_row(self, current_row, data_frame, data_of_given_row):
        for current_attribute in range(0, len(self.bookAttributes)):
            data_of_given_row.append(data_frame.at[current_row, self.bookAttributes[current_attribute]])
        self.books_from_csv.append(data_of_given_row)

