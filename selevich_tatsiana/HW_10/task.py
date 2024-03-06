from constants import *


class Book:
    def __init__(self, name: str, author_name: str, pages: int, isbn: int) -> None:
        """
        :param name: name book
        :param author_name: author name
        :param pages: number of pages
        :param isbn: ISBN of book
        """
        self.name = name
        self.author_name = author_name
        self.pages = pages
        self.isbn = isbn
        self.is_booked = False
        self.is_taken = False

    def __str__(self):
        return f"{self.name}, {self.author_name}, {self.isbn}"


class User:
    def __init__(self, personal_number: int, name: str, surname: str) -> None:
        """
        :param personal_number: user's personal number
        :param name: user's name
        :param surname: user's surname
        """
        self.personal_number = personal_number
        self.name = name
        self.surname = surname

    @staticmethod
    def take_book(book: Book) -> None:
        """
        This is a method that allows to take a book.
        :param book: book
        """
        if book.is_booked or book.is_taken:
            print("Error: The book has already been taken or booked.")
        else:
            book.is_booked = True
            book.is_taken = True

    @staticmethod
    def return_book(book: Book) -> None:
        """
        This is a method that allows to return a book.
        :param book: book
        """
        book.is_booked = False
        book.is_taken = False

    @staticmethod
    def reserve_book(book: Book) -> None:
        """
        This is a method that allows to reserve a book.
        :param book: book
        """
        if book.is_booked or book.is_taken:
            print("Error: The book has already been taken or booked.")
        else:
            book.is_booked = True

    @staticmethod
    def cancel_book(book: Book) -> None:
        """
        This is a method that allows to cancel a book reservation.
        :param book: book
        """
        book.is_booked = False


book1 = Book(FIRST_BOOK_NAME, FIRST_AUTHOR_NAME, FIRST_BOOK_PAGES, FIRST_BOOK_ISBN)
book2 = Book(SECOND_BOOK_NAME, SECOND_AUTHOR_NAME, SECOND_BOOK_PAGES, SECOND_BOOK_ISBN)
book3 = Book(THIRD_BOOK_NAME, THIRD_AUTHOR_NAME, THIRD_BOOK_PAGES, THIRD_BOOK_ISBN)

user1 = User(FIRST_USER_PERSONAL_NUMBER, FIRST_USER_NAME, FIRST_USER_SURNAME)
user2 = User(SECOND_USER_PERSONAL_NUMBER, SECOND_USER_NAME, SECOND_USER_SURNAME)
user3 = User(THIRD_USER_PERSONAL_NUMBER, THIRD_USER_NAME, THIRD_USER_SURNAME)

user1.reserve_book(book1)
user2.reserve_book(book1)
