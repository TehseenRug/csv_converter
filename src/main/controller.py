from flask import Flask

from src.main.csv_service import CSVService

app = Flask(__name__)

# here we probably should return a json string containing all books as dtos

@app.route('/')
def get_books_from_csv():
    csv_service = CSVService()
    result = csv_service.get_books_from_csv()
    return result


if __name__ == '__main__':
    app.run(threaded=False)