from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pydantic.dataclasses import dataclass
from dataclasses import field
import mysql.connector
import uuid
import uvicorn
import uuid

from models.book import Book
from book_repository import BookRepository
from database.db import connect_db

app = FastAPI()


db = connect_db()
book_repository = BookRepository(db)


@app.post("/books/")
async def create_book(book: Book):
    book = book_repository.save(Book(book.title))
    return book


@app.get("/books/{book_id}")
def read_book(book_id: str):
    book = book_repository.find_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}")
def update_book_status(book_id: str, book: Book):
    updated_book = book_repository.update_by_status(book_id, book.status)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    deleted = book_repository.delete(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}


@app.get("/books")
def get_books_by_status(status: str):
    if status:
        books = book_repository.find_all_by_status(status)
        return books


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=3000,
                reload=True, access_log=False)
