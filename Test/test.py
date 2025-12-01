# test_client.py
import requests

BASE_URL = "http://127.0.0.1:5000"

# 1) POST: create a new book
new_book = {
    "isbn": 3,
    "title": "Test Book",
    "author": "Tester",
    "year_published": 2020,
    "price": 10.5,
    "in_stock": 5,
}

post_res = requests.post(f"{BASE_URL}/books", json=new_book)
print("POST status:", post_res.status_code)
print("POST body:", post_res.json())

# 2) GET: fetch all books
get_res = requests.get(f"{BASE_URL}/books")
print("GET status:", get_res.status_code)
print("GET body:", get_res.json())