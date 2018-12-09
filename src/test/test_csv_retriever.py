from unittest import TestCase

class TestCSVRetriever(TestCase):
    pass

    def test_numbers_3_4(self):
        self.assertEqual(3 * 4, 12)

    # noinspection PyUnusedLocal
    #@patch('src.main.csv_helper.CSVHelper.add_up_two_number', return_value=19)
    #def test_uses_helper(self, add_up_two_number):
    #    csv_retriever = CSVRetriever(CSVHelper())
    #    mock_result = csv_retriever.add_with_mock(8, 2)
    #    self.assertEqual(mock_result, 19)
