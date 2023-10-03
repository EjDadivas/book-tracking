import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def test_data():
    # You can set up any test data or fixtures here
    pass

book_id = ""

def test_create_book():
    global book_id  # Use the global keyword to modify the global variable
    response = client.post("/books/", json={"title": "Test Book"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"
    book_id = response.json()["id"]
    print(book_id)

def test_read_book():
    global book_id  # Use the global keyword to access the global variable
    # Assuming you have a book_id from a previous test or setup
    # book_id = "your_test_book_id"
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200

def test_update_book_status():
    global book_id  # Use the global keyword to access the global variable
    # Assuming you have a book_id from a previous test or setup
    response = client.put(f"/books/{book_id}", json={"title": "","status": "completed"})
    assert response.status_code == 200
    assert response.json()["status"] == "completed"

def test_delete_book():
    global book_id  # Use the global keyword to access the global variable
    # Assuming you have a book_id from a previous test or setup
    # book_id = "your_test_book_id"
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted"

def test_get_books_by_status():
    # Assuming you have a valid status to test
    status = "completed"
    response = client.get(f"/books?status={status}")
    assert response.status_code == 200
    # You can assert the response data as needed

if __name__ == "__main__":
    pytest.main()
