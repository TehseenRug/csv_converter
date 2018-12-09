import pandas as pd

class CSVRetriever:

    books_from_csv = []
    bookAttributes = ['MainTitle', 'SubTitle', 'FirstName', 'LastName', 'MainGenre', 'SubGenre', 'AppearanceYear']

    def retrieve(self):
        data_frame = pd.read_csv('../resources/books.csv')
        print(data_frame)
        count_row = data_frame.shape[0]

        data_of_given_row = []
        for j in range(0, count_row - 1):
            for i in range(0, len(self.bookAttributes) - 1):
                print(i)
                print(self.bookAttributes[i])
                data_of_given_row.append(data_frame.at[j, self.bookAttributes[i]])
            self.books_from_csv.append(data_of_given_row)
            data_of_given_row = []
        print(self.books_from_csv)
        return self.books_from_csv

