# File: D:\SEL\CICD\test_code\test_pp1.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src_code')))
from fastapi.testclient import TestClient
from ppTest import api  # Import your FastAPI app (change filename if different)

client = TestClient(api)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Book Management System"}

def test_add_book():
    book_data = {
        "id": 1,
        "name": "Book One",
        "description": "First test book",
        "isAvailable": True
    }
    response = client.post("/book", json=book_data)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Book One"

def test_get_books():
    response = client.get("/book")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    assert len(books) >= 1

def test_update_book():
    updated_data = {
        "id": 1,
        "name": "Book One Updated",
        "description": "Updated description",
        "isAvailable": False
    }
    response = client.put("/book/1", json=updated_data)
    assert response.status_code == 200
    book = response.json()
    assert book["name"] == "Book One Updated"
    assert book["isAvailable"] is False

def test_delete_book():
    response = client.delete("/book/1")
    assert response.status_code == 200
    deleted_book = response.json()
    assert deleted_book["id"] == 1

def test_delete_non_existing_book():
    response = client.delete("/book/999")
    assert response.status_code == 200
    assert response.json() == {"error": "Book not found, deletion failed"}
