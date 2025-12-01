from flask import Flask, jsonify, request
from datetime import datetime
from database import db
from models import Book


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# Sample data

with app.app_context():
    db.create_all()

@app.route('/')
def Home():

    return "Welcome to the Book Store!"
    # Here you would normally handle the home route

@app.route("/books", methods=["GET", "POST"])
def books_route():
    all_books = Book.query.all()
    if request.method == "GET":
        all_books = Book.query.all()          # ask the DB for all rows
        books_data = [book.to_dict() for book in all_books]
        return jsonify(books_data), 200
        # Here you would normally handle fetching books
    elif request.method == "POST":
        today = datetime.now().year
        #first check if the book exists so we will take the id from the json file and we will check if it exists
        data = request.get_json()
        found = False
        for book in all_books:
            if book.isbn == data.get("isbn"):
                found = True;
        if found:
            return jsonify({"message": "Book with this ID already exists."}), 400
        else:
            if data.get("isbn") is None or data.get("title") is None or data.get("author") is None or data.get("year_published") is None or data.get("price") is None or data.get("in_stock") is None:
                return jsonify({"message": "Missing data for one or more fields."}), 400
            elif data.get("year_published") < 1450 or data.get("year_published") > today:
                return jsonify({"message": "Wrong year"}), 400
            elif data.get("price") < 0:
                return jsonify({"message": "Price cannot be negative"}), 400
            elif data.get("in_stock") < 0:
                return jsonify({"message": "In-stock quantity cannot be negative"}), 400
            new_book = Book(
            isbn=data.get("isbn"),
            title=data.get("title"),
            author=data.get("author"),
            year_published=data.get("year_published"),
            price=data.get("price"),
            in_stock=data.get("in_stock"),
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201
def book_detail(isbn):
    book = Book.query.get(isbn)
    if book is None:
        return jsonify({"message": "Book not found"}), 404
    if request.method == "GET":
        return jsonify(book.to_dict()), 200
    elif request.method == "PUT":
        data = request.get_json()
        today = datetime.now().year
        if data.get("title") is None or data.get("author") is None or data.get("year_published") is None or data.get("price") is None or data.get("in_stock") is None:
            return jsonify({"message": "Missing data for one or more fields."}), 400
        elif data.get("year_published") < 1450 or data.get("year_published") > today:
            return jsonify({"message": "Wrong year"}), 400
        elif data.get("price") < 0:
            return jsonify({"message": "Price cannot be negative"}), 400
        elif data.get("in_stock") < 0:
            return jsonify({"message": "In-stock quantity cannot be negative"}), 400
        book.title = data.get("title")
        book.author = data.get("author")
        book.year_published = data.get("year_published")
        book.price = data.get("price")
        book.in_stock = data.get("in_stock")
        db.session.commit()
        return jsonify(book.to_dict()), 200
    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted"}), 200
    
            