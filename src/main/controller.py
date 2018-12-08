from flask import Flask

from src.main.csv_service import CSVService

app = Flask(__name__)


@app.route('/')
def get_books_from_csv():
    csv_service = CSVService()
    return csv_service.get_books_from_csv()