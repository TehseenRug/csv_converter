import pandas as pd

from src.main.csv_helper import CSVHelper


class CSVRetriever:

    csv_helper = CSVHelper()

    def add(self, x, y):
        return x + y

    def add_with_mock(self, x, y):
        return self.csv_helper.add_up_two_number(x, y)
