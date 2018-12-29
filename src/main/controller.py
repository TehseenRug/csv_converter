from flask import Flask, json

from src.main.csv_service import CSVService

csv_service = CSVService()
app = Flask(__name__)
books = csv_service.get_books_from_csv()


@app.route('/')
def get_books_from_csv():
    return json.dumps(books, default=lambda x: x.__dict__)


if __name__ == '__main__':
    app.run(threaded=True)
