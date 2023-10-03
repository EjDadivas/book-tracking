import uuid
import mysql.connector
from typing import List
from models.book import Book
from dataclasses import dataclass, field
import uuid


class BookRepository:
    def __init__(self, db_connection):
        self.conn = db_connection
        self.cursor = self.conn.cursor()

    def save(self, book: Book) -> Book:
        query = "INSERT INTO books (id, title, status) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (str(book.id), book.title, book.status))
        self.conn.commit()
        return book

    def find_by_id(self, book_id: uuid.UUID) -> Book:
        query = "SELECT * FROM books WHERE id = %s"
        self.cursor.execute(query, (str(book_id),))
        row = self.cursor.fetchone()
        if row:
            book_id, title, status = row
            return Book(id=uuid.UUID(book_id), title=title, status=status)
        return None

    def exists(self, book_id: uuid.UUID) -> bool:
        book = self.find_by_id(book_id)
        return book is not None

    def update_by_status(self, book_id: uuid.UUID, status: str) -> Book:
        query = "UPDATE books SET status = %s WHERE id = %s"
        self.cursor.execute(query, (status, book_id))
        self.conn.commit()
        book = self.find_by_id(book_id)
        return book

    def delete(self, book_id: uuid.UUID) -> bool:
        query = "DELETE FROM books WHERE id = %s"
        self.cursor.execute(query, (str(book_id),))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def find_all(self) -> List[Book]:
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Book(id=uuid.UUID(book_id), title=title, status=status) for book_id, title, status in rows]

    def find_all_by_status(self, status: str) -> List[Book]:
        query = 'SELECT * FROM books WHERE status = %s'
        self.cursor.execute(query, (status,))
        rows = self.cursor.fetchall()

        return [Book(id=uuid.UUID(book_id), title=title, status=status) for book_id, title, status in rows]
