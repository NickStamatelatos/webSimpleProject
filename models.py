from database import db

class Book(db.Model):
    
    __tablename__ = 'books'

    isbn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "year_published": self.year_published,
            "price": self.price,
            "in_stock": self.in_stock,
        }
