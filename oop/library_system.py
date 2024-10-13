# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size  # Initialize the specific attribute for EBook

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count  # Initialize the specific attribute for PrintBook

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []  # List to store instances of Book, EBook, and PrintBook

    def add_book(self, book: Book):
        self.books.append(book)  # Add the book to the collection

    def list_books(self):
        for book in self.books:
            print(book)  # Print details of each book

