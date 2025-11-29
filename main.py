from models import Book
from flask import Flask, jsonify
import request
from datetime import datetime

app = Flask(__name__)

# Sample data
books = [
    Book(1, "Dune", "Frank Herbert", 1965, 9.99, 3),
    Book(2, "Something", "James Cordel", 1967, 97.99, 37),
]


@app.route('/')
def Home():
    return "Welcome to the Book Store!"
    # Here you would normally handle the home route

@app.route("/books", methods=["GET", "POST"])
def books():
    if request.method == "GET":
        books_data = [book.to_dict() for book in books]
        return jsonify(books_data), 200
        # Here you would normally handle fetching books
    elif request.method == "POST":
        today = datetime.now().year
        #first check if the book exists so we will take the id from the json file and we will check if it exists
        data = request.get_json()
        found = False
        for book in books:
            if book.isbn == data.get("isbn"):
                found = True;
        if found:
            return jsonify({"message": "Book with this ID already exists."}), 400
        else:
            if data.get("isbn") is None or data.get("title") is None or data.get("author") is None or data.get("year_published") is None or data.get("price") is None or data.get("in_stock") is None:
                return jsonify({"message": "Missing data for one or more fields."}), 400
            elif data.get("year_published") < 1450 and data.get("year_published") > today:
                return jsonify({"message": "Wrong year"}), 400
            elif data.get("price") < 0:
                return jsonify({"message": "Price cannot be negative"}), 400
            elif data.get("in_stock") < 0:
                return jsonify({"message": "In-stock quantity cannot be negative"}), 400
            new_book = Book(
                data.get("isbn"),
                data.get("title"),
                data.get("author"),
                data.get("year_published"),
                data.get("price"),
                data.get("in_stock"),
            )
            books.append(new_book)
            return jsonify(new_book.to_dict()), 201
@app.route("/books/<int:isbn>", methods=["GET", "PUT", "DELETE"])
def book_detail(isbn):
    try:
        for book in books:
            if book.isbn == isbn:
                if request.method == "GET":
                    return jsonify(book.to_dict()), 200
                elif request.method == "PUT":
                    data = request.get_json()
                    today = datetime.now().year
                    if data.get("title") is not None:
                        book.title = data.get("title")
                    if data.get("author") is not None:
                        book.author = data.get("author")
                    if data.get("year_published") is not None:
                        if data.get("year_published") < 1450 or data.get("year_published") > today:
                            return jsonify({"message": "Wrong year"}), 400
                        book.year_published = data.get("year_published")
                    if data.get("price") is not None:
                        if data.get("price") < 0:
                            return jsonify({"message": "Price cannot be negative"}), 400
                        book.price = data.get("price")
                    if data.get("in_stock") is not None:
                        if data.get("in_stock") < 0:
                            return jsonify({"message": "In-stock quantity cannot be negative"}), 400
                        book.in_stock = data.get("in_stock")
                    return jsonify(book.to_dict()), 200
                elif request.method == "DELETE":
                    books.remove(book)
                    return jsonify({"message": "Book deleted"}), 200
    catch(exception e):
        return jsonify({"message": "Book not found"}), 404
    
            