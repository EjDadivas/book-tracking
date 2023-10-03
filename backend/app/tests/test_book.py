import unittest
from models.book import Book  # Update the import statement

class TestBook(unittest.TestCase):

    def test_book_creation(self):
        # Create a Book instance
        book = Book(title="Sample Book", status="Available")

        # Check if the title and status match
        self.assertEqual(book.title, "Sample Book")
        self.assertEqual(book.status, "Available")

    def test_book_id_generation(self):
        # Create two Book instances
        book1 = Book(title="Book 1", status="Available")
        book2 = Book(title="Book 2", status="Checked Out")

        # Check if the IDs are unique
        self.assertNotEqual(book1.id, book2.id)

if __name__ == '__main__':
    unittest.main()
