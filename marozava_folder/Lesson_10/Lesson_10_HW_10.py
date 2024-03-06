# Classwork
# class Worker:
#
#     number_of_workers = 0
#
#     def __init__(self, name: str, salary: int):
#         Worker.number_of_workers += 1
#         self.name = name
#         self.salary = salary
#
#     @property
#     def worker_name(self):
#         return self.name
#
#     def __str__(self):
#         return f"My name is {self.name}. My salary is {self.salary}"
#
#     def __gt__(self, other):
#         return self.salary > other.salary
#
#
# mik = Worker('Mik', 10_000)
# jim = Worker('Jim', 20_000)
#
# print()


# Домашка.
#
# Создайте класс book с именем книги, автором, кол - м страниц, ISBN(инвентарный номер - например 6 - ти значное число),
# флагом, зарезервирована ли книга или нет(если хотите, вы можете добавить еще свойств чтобы ваша
# реализация работала как задумано вами).Плюс еще один флаг - на руках ли книга или свободна. Все эти свойства класса
# задаются при создании класса через конструктор, не через инпуты.

# Добавить перегрузку метода str чтобы при принте экземпляра класса выдавалась информация о книге(хотя бы название, но
# можно добавить что - нибудь еще) Создайте класс пользователь который может брать книгу, возвращать, бронировать и
# снимать бронь(создайте методы у класса  пользователь для этих действий). Если один пользователь забронировал или
# читает книгу, второй пользователь не может  бронировать или брать ее.

class Book:
    def __init__(self, name: str, writer: str, num_pages: int, isbn: int):
        self.name = name
        self.writer = writer
        self.num_pages = num_pages
        self.isbn = isbn
        self.__is_reserved = False
        self.__is_free = True

    @property
    def is_reserved(self):
        return self.__is_reserved

    @property
    def is_free(self):
        return self.__is_free

    @is_free.setter
    def is_free(self, value):
        self.__is_free = value

    @is_reserved.setter
    def is_reserved(self, value):
        self.__is_reserved = value

    def __str__(self):
        return f"Book '{self.name}' which wrote {self.writer}. Number of pages: {self.num_pages}, ISBN: {self.isbn}"


class Reader:

    def __init__(self, name: str):
        self.name = name
        self.reserved_book = None
        self.taken_book = None

    def take_book(self, book: Book):
        if not book.is_free or book.is_reserved:
            print(f'User {self.name} cannot take a book {book.name}')
        else:
            book.is_free = False
            self.taken_book = book
            print(f'User {self.name} took a book {book.name}')

    def reserve_book(self, book: Book):
        if book.is_reserved or not book.is_free:
            print(f'User {self.name} cannot reserve a book {book.name}')
        else:
            book.is_reserved = True
            self.reserved_book = book
            print(f'User {self.name} reserved a book {book.name}')

    def return_book(self):
        if self.taken_book is not None:
            self.taken_book.is_free = True
            print(f'User {self.name} returned a book {self.taken_book.name}')
        else:
            print('Nothing to return')

    def un_reserve(self):
        if self.reserved_book is not None:
            self.reserved_book.is_reserved = False
            print(f'User {self.name} canceled the reservation for book {self.reserved_book.name}')
        else:
            print('The book is already reserved')


book = Book('Harry Potter and the philosophers stone', 'J.K. Rowling', 500, 100222)
print(book)
# book2 = Book('Lord of the Rings', 'Tolkien J.R.R.', 780, 100333)
user = Reader('Vika')
user2 = Reader('Sergey')
user.take_book(book)
user2.reserve_book(book)
user.return_book()
user2.return_book()
user2.take_book(book)


