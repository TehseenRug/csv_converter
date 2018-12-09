from src.main.csv_retriever import CSVRetriever


class CSVService:

    def __init__(self):
        self.csv_retriever = CSVRetriever()

    def get_books_from_csv(self):
        self.csv_retriever.retrieve()
        return []