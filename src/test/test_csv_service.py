from unittest import TestCase
from unittest.mock import patch

from src.main.csv_service import CSVService


class TestCSVService(TestCase):
    pass

    @patch('src.main.csv_retriever.CSVRetriever.retrieve')
    def test_get_books_from_csv_service(self, retrieve):
            csv_service = CSVService()
            csv_service.get_books_from_csv()
            retrieve.assert_called_once_with()