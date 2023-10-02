import unittest
from models.models import Book


class TestBook(unittest.TestCase):

    def test_book_creation(self):
        # Create a Book instance
        book = Book(title="Sample Book", status="to-read")

        # Check if the title and status match
        self.assertEqual(book.title, "Sample Book")
        self.assertEqual(book.status, "to-read")

    def test_book_id_generation(self):
        # Create two Book instances
        book1 = Book(title="Book 1", status="to-read")
        book2 = Book(title="Book 2", status="in-progress")

        # Check if the IDs are unique
        self.assertNotEqual(book1.id, book2.id)


if __name__ == '__main__':
    unittest.main()
