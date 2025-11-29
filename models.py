class Book:
    def __init__(self,isbn, title, author, year_published, price, in_stock):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year_published = year_published
        self.price = price
        self.in_stock = in_stock

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "year_published": self.year_published,
            "price": self.price,
            "in_stock": self.in_stock,
        }
