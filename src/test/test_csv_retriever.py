from unittest import TestCase
from unittest.mock import patch

from src.main.csv_retriever import CSVRetriever


class TestCSVRetriever(TestCase):
    pass

    def setUp(self):
        pass

    def test_adds_two_numbers(self):
        csv_retriever = CSVRetriever()
        result = csv_retriever.add(5, 9)
        print(result)
        self.assertIs(result, 14)

    def test_numbers_3_4(self):
        print('halllo')
        self.assertEqual(3 * 4, 12)

    # noinspection PyUnusedLocal
    @patch('src.main.csv_helper.CSVHelper.add_up_two_number', return_value=19)
    def test_uses_helper(self, add_up_two_number):
        csv_retriever = CSVRetriever()
        mock_result = csv_retriever.add_with_mock(8, 12)
        self.assertEqual(mock_result, 19)
