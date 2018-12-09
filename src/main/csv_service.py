from src.main.csv_retriever import CSVRetriever


class CSVService:

    def __init__(self):
        self.csv_retriever = CSVRetriever()

    # after retriever all data, the data still needs to be converted to json

    def get_books_from_csv(self):
        return self.csv_retriever.retrieve()