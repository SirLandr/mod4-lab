from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///data.db'
db = SQLAlchemy(app)

class book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.author} - {self.publisher}"

@app.route('/Book')
def get_book():
    book = book.query.all()

    output = []
    for book in book:
        book_data = {'name': book.name, 'author': book.author, 'publisher': book.publisher}

        output.append(book.data)
        
    return{"book": book}
