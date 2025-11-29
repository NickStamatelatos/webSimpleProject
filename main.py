from models import Book
from flask import Flask, jsonify

app = Flask(__name__)

books = [
    Book(1, "Dune", "Frank Herbert", 1965, 9.99, 3),
    Book(2, "Something", "James Cordel", 1967, 97.99, 37),
]


@app.route('/')
def Home():
    return "Welcome to the Book Store!"

@app.route("/books")
def get_books():
    books_data = [book.to_dict() for book in books]
    return jsonify(books_data)