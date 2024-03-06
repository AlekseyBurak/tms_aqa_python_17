"""
Создайте класс book с именем книги, автором, кол-м страниц, ISBN (инвентарный номер - например 6-ти значное число),
флагом, зарезервирована ли книга или нет (если хотите, вы можете добавить еще свойств чтобы ваша реализация

Все эти свойства класса задаются при создании класса через конструктор, не через инпуты.

Добавить перегрузку метода str чтобы при принте экземпляра класса выдавалась информация о книге
(хотя бы название, но можно добавить что-нибудь еще)

Создайте класс пользователь который может брать книгу, возвращать, бронировать и снимать бронь
(создайте методы у класса пользователь для этих действий).
Если один  пользователь забронировал или читает книгу, второй пользователь не может бронировать или брать ее.
"""
class Book:
    def __init__(self, name_of_book: str, author: str, pages: int, isbn: int, reserved=False, availability=False):
        self.name_of_book = name_of_book
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved
        self.availability = availability

    def __str__(self):
        return (f"Name of book: {self.name_of_book}, Author: {self.author}, pages: {self.pages}, ISBN: {self.isbn}"
                f"\nstatus: {self.reserved}, {self.availability}")
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_book = None
        self.reserved_book = None

    def borrow(self, book):
        if not book.reserved and not book.availability:
            book.availability = True
            self.borrowed_book = book
            print(f"{self.name} borrowed '{book.name_of_book}'.")
        else:
            print(f"Sorry, '{book.name_of_book}' is not available for borrowing.")

    def return_book(self):
        if self.borrowed_book:
            self.borrowed_book.availability = False
            print(f"{self.name} returned '{self.borrowed_book.name_of_book}'.")
            self.borrowed_book = None
        else:
            print(f"{self.name}, you don't have any borrowed books.")

    def reserve(self, book):
        if not book.reserved and not book.availability:
            book.reserved = True
            self.reserved_book = book
            print(f"{self.name} reserved '{book.name_of_book}'.")
        else:
            print(f"Sorry, '{book.name_of_book}' is not available for reservation.")

    def cancel_reservation(self):
        if self.reserved_book:
            self.reserved_book.reserved = False
            print(f"{self.name} canceled the reservation for '{self.reserved_book.name_of_book}'.")
            self.reserved_book = None
        else:
            print(f"{self.name}, you don't have any reserved books.")

book1 = Book(name_of_book="Pride and Prejudice", author="Jane Austen", pages=376, isbn=123456)
print(book1)
book2 = Book(name_of_book="Harry Potter", author="Joanne Kathleen Rowling", pages=405, isbn=654321)
print(book2)

user1 = User("Anna")
user2 = User("Lena")

user1.borrow(book1)
user2.reserve(book1)
user2.borrow(book1)  # Book is reserved
user1.return_book()

user2.borrow(book1)  # Should succeed now
user2.cancel_reservation()




