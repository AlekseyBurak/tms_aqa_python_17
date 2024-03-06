# Создайте класс book с именем книги, автором, кол-м страниц, ISBN (инвентарный номер - например 6-ти значное число),
# флагом, зарезервирована ли книга или нет (если хотите, вы можете добавить еще свойств
# чтобы ваша реализация работала как задумано вами). Плюс еще один флаг - на руках ли книга или свободна.

# Все эти свойства класса задаются при создании класса через конструктор, не через инпуты.

# Добавить перегрузку метода str чтобы при принте экземпляра класса выдавалась информация о книге
# (хотя бы название, но можно добавить что-нибудь еще)

# Создайте класс пользователь который может брать книгу, возвращать, бронировать и снимать бронь
# (создайте методы у класса пользователь для этих действий).
# Если один  пользователь забронировал или читает книгу, второй пользователь не может бронировать или брать ее.



class Book:

    def __init__(self, name_of_book: str, page_count: int, author: str, ISBN: int):
        self.ISBN = ISBN
        self.author = author
        self.page_count = page_count
        self.name_of_book = name_of_book

    @property
    def number_of_pages(self):
        return self.page_count

    @property
    def author_of(self):
        return self.author

    @property
    def name_book(self):
        return self.name_of_book

    @property
    def inventory(self):
        return self.ISBN

    @staticmethod
    def go():
        print(f'You have to read this book in English')


class Change_1:
    flag = None

    def __init__(self):
        self.flag = True


def change_flag(other):
    other.flag = False


class Change_2:
    pass


my_book = Book("Harry Potter and philosopher`s stone", 255, "J.K. Rowling", 367536)
print(f"My book is called {my_book.name_of_book}. It has {my_book.page_count} pages.\n"
      f"It was written by an author {my_book.author}. Its ISBN {my_book.ISBN}")
my_change = Change_1()
my_change1 = Change_2()

print(my_change.flag)
change_flag(my_change)
print(my_change.flag)

print(Book.go())
