from flask import Flask

csv_service = CSVService()
app = Flask(__name__)

@app.route('/')
def get_books_from_csv():
    return 'hello world'


if __name__ == '__main__':
    app.run(threaded=True)
