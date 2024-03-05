'''
     name - название книги
     author - автор книги
     pages - количество страниц
     IBN - инвентарный номер
     reserve - резервация книги
     flag - на руках книга или свободна
'''
class Book:
    def __init__(self, name: str, author: str, pages: int, IBN: str, reserve: bool, flag: bool):
        self.name = name
        self.author = author
        self.pages = pages
        self.IBN = IBN
        self.reserve = reserve
        self.flag = flag

    def __str__(self):
        return f"This is book {self.name}. Number of the pages: {self.pages}"

book1 = Book("Tom and Jeery", "Tom Cruse", "35", "3654123", "True", "False")
print(book1)

class User(Book):
    def __init__(self, userName: str):
        self.userName = userName
    def __init__
