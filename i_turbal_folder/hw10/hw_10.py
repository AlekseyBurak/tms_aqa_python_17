class Book:
    def __init__(self, book_name: str, autor: str, number_of_pages: int, isbn: int,
                 is_taken=False, is_reserved=False):
        self.book_name = book_name
        self.autor = autor
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.is_taken = is_taken
        self.is_reserved = is_reserved

    def __str__(self):
         return (f"Book: {self.book_name}\n"
                f"Autor: {self.autor}\n"
                f"ISBN: {self.isbn}")
    @property
    def protected(self):
        return self.isbn

class Reader():
    def __init__(self, name):
        self.name = name


    def reserve_book(self, book):
        if not book.is_taken or not book.is_reserved:
            book.is_reserved = True
            print(f"You reserved the '{book.book_name}'")
        else:
            print(f"The book '{book.book_name}' is already reserved")
    def take_book(self, book):
        if not book.is_taken and not book.is_reserved:
            book.is_taken = True
            print(f"You took the '{book.book_name}'")

        elif book.is_taken:
            print(f"The book '{book.book_name}' is already taken")
        elif book.is_reserved:
            print(f"YOu can't take the book '{book.book_name}', it is reserved")
    def unreserve_book(self, book):
        if book.is_reserved:
            book.is_reserved = False
            print(f"Book '{book.book_name}' is unreserved")
        else:
            print(f'Error')
    def return_book(self, book):
        if book.is_taken:
            book.is_taken = False
            print(f"Thanks for  return '{book.book_name}'. See u next tine")
        else:
            print("error")


book1 = Book("Магические методы и места, где они обитают", 'Igor', 123, 231 )
book2 = Book("Гарри Поттер и основы ООП ", 'Алексей Бурак', 123, 231 )
user1 = Reader("Ron")
user2 = Reader('Golum')
print(book1)
user1.take_book(book1)
print(book1.is_reserved)
user2.return_book(book1)
user2.return_book(book1)
user2.reserve_book(book2)
user2.unreserve_book(book2)
user2.unreserve_book(book2)
