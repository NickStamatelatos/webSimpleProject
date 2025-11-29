class Book:
    def __init__(self,book_id, title, author, year_published, price, in_stock):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year_published = year_published
        self.price = price
        self.in_stock = in_stock

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year_published": self.year_published,
            "price": self.price,
            "in_stock": self.in_stock,
        }
