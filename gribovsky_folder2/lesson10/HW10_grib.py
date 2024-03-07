class Library:
    class Book:
        def __init__(self, title: str, author: str, pages: int, ISBN: int, reserved: bool) -> None:
            self.title = title
            self.author = author
            self.pages = pages
            self.ISBN = ISBN
            self.reserved = False
            self.reading = False

        def __str__(self) -> str:
            return f"Book - {self.title}, author - {self.author}"

    class User:
        def __init__(self, name: str) -> None:
            self.name = name

        def __str__(self):
            return self.name

        def get_book(self, book):
            if not book.reading and not book.reserved:
                print(f"{self.name} took {book.title}")
                book.reading = True
                book.reserved = True
            else:
                print(f"{book.title} забронирована или выдана на руки")

        def return_book(self, book):
            print(f"{self.name} returned {book.title}")
            book.reading = False
            book.reserved = False

        def book_book(self, book):
            if book.reserved:
                print(f"{book.title} забронирована другим пользователем")
            else:
                print(f"{self.name} может забронировать {book.title}")
                reserved = False


chemistry = Library.Book("Химия 8 класс", "Фельдман Ф.Г., Рудзитис Г.Е", 158, 666555, False)
vasya = Library.User("Vasya Pupkin")
petya = Library.User("Petya Pupkin")
# print(chemistry)
# print(vasya)
vasya.get_book(book=chemistry)
petya.get_book(chemistry)
petya.book_book(chemistry)
vasya.return_book(chemistry)
petya.get_book(chemistry)
