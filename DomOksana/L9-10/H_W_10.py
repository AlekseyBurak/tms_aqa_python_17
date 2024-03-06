class Book:
    def __init__(self, name, author, pages, isbn, reserved=False, on_hand=False):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved
        self.on_hand = on_hand

    def __str__(self):
        return f"Название: {self.name}, Автор: {self.author}, Страниц: {self.pages}, ISBN: {self.isbn}"

class User:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, book):
        if book.reserved or book.on_hand:
            return "Книга уже забронирована или на руках у другого пользователя."
        else:
            book.on_hand = True
            return f"{self.name} взял книгу {book.name}."

    def return_book(self, book):
        if book.on_hand:
            book.on_hand = False
            return f"{self.name} вернул книгу {book.name}."
        else:
            return "Эта книга не на руках у пользователя."

    def reserve_book(self, book):
        if book.reserved or book.on_hand:
            return "Книга уже забронирована или на руках у другого пользователя."
        else:
            book.reserved = True
            return f"{self.name} забронировал книгу {book.name}."

    def unreserve_book(self, book):
        if book.reserved:
            book.reserved = False
            return f"{self.name} снял бронь с книги {book.name}."
        else:
            return "Эта книга не была забронирована."


book1 = Book("Война и мир", "Лев Толстой", 1225, 123456)
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 525, 234567)
book3 = Book("Лолита", "Владимир Набоков", 325, 345678)

user1 = User("Иванов")
user2 = User("Петров")

print(book1)
print(book2)
print(book3)

print(user1.borrow_book(book1))
print(user2.borrow_book(book2))
print(user1.borrow_book(book2)) #эту книгу уже не возьмет

print(user1.reserve_book(book3))
print(user2.borrow_book(book3)) #эту книгу уже не возьмет
print(user1.unreserve_book(book3))
print(user2.borrow_book(book3)) #сейчас эту книгу уже можно взять
print(user1.reserve_book(book3)) #эту книгу уже не забронируешь