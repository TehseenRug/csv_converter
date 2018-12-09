import pandas as pd

class CSVRetriever:


    # retrieve all data from all rows and set them as params of dtos in all books
    def retrieve(self):
        data_frame = pd.read_csv('../resources/books.csv')
        title_of_first_entry = data_frame.at[0, 'MainTitle']
        return title_of_first_entry

