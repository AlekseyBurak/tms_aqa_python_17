

class LibrarianError(Exception):
    pass


class Book:

    def __init__(self, author: str, title: str, isbn: str, pages: int):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.pages = pages
        self.__booked = False
        self.__borrowed = False

    def __str__(self):
        return f"{self.author} - {self.title} - {self.isbn} - {self.pages}"

    @property
    def booked(self):
        return self.__booked

    @booked.setter
    def booked(self, value):
        if isinstance(value, bool):
            self.__booked = value
        else:
            raise LibrarianError("Booked must be boolean")

    @property
    def borrowed(self):
        return self.__borrowed

    @borrowed.setter
    def borrowed(self, value):
        if isinstance(value, bool):
            self.__borrowed = value
        else:
            raise LibrarianError("Borrowed must be boolean")


class Reader:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.borrowed_books = []
        self.booked_books = []

    def __str__(self):
        if self.borrowed_books:
            return f"My name is {self.name} - I'm {self.age} years old -- my borrowed books {[str(book) for book in self.borrowed_books]}"
        else:
            return f"My name is {self.name} - I'm {self.age} years old -- i have no borrowed books"

    def borrow_book(self, book: Book):
        if book.booked or book.borrowed:
            raise LibrarianError("Book is already borrowed or booked")
        else:
            book.borrowed = True
            self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            raise LibrarianError("Book is not borrowed")
        else:
            book.borrowed = False
            self.borrowed_books.remove(book)

    def book_book(self, book: Book):
        if book.booked or book.borrowed:
            raise LibrarianError("Book is already borrowed or booked")
        else:
            book.booked = True
            self.booked_books.append(book)

    def unbook_book(self, book: Book):
        if book not in self.booked_books:
            raise LibrarianError("Book is not booked")
        else:
            book.booked = False
            self.booked_books.remove(book)


book = Book("Tolken", "The Lord of the Rings", "978-1-42", 1000)


alex = Reader("Alex", 29)
# not_alex = Reader("Not Alex", 30)
#
alex.borrow_book(book)
# # not_alex.borrow_book(book)
# alex.return_book(book)

print(alex)
# alex.book_book(book)

# alex.unbook_book(book)

# not_alex.borrow_book(book)