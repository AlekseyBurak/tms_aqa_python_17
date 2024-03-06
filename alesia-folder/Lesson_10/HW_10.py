class Book:

   NUMBER_OF_BOOKS = 0
   def __init__(self, name: str, author: str, isbn: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = False
        self.taken = False
        Book.NUMBER_OF_BOOKS += 1

   def __str__(self):
        return f"This is '{self.name}' by {self.author}."

class User:
    def __init__(self, user_name: str):
        self.user_name = user_name

    def take_book (self, other):
        if other.taken == False and other.reserved == False:
            other.taken = True
            print(f"{self.user_name} took '{other.name}'.")
        else:
            print(f"{self.user_name} can't take '{other.name}' as it was taken or reserved by someone else.")
    def return_book(self, other):
        other.taken = False
        print(f"'{other.name}' was returned by {self.user_name}.")
    def reserve_book(self, other):
        if other.reserved == False:
            other.reserved = True
            print(f"{self.user_name} reserved '{other.name}'.")
        else:
            print(f"This book is reserved by someone else.")
    def cancel_reserve(self, other):
        other.reserved = False
        print(f"{self.user_name} canceled reservation of '{other.name}'.")



book1 = Book("Jane Eyre", "Charlotte Bronte",  "978-1604594119", 570)
book2 = Book("Three Men in a Boat (To Say Nothing of the Dog)", "Jerome K Jerome", "0-7195-4089-5", 290)
book3 = Book("Nineteen Eighty-Four", "George Orwell", "978-0-06-181088-6", 320)
john = User("John Smith")
paul = User("Paul Newman")
george = User("George Wash")
print(f"Total number of the books in the library: {Book.NUMBER_OF_BOOKS}")
print(book1)
print(book2)
print(book3)
print()
john.take_book(book1)
paul.take_book(book1)
paul.reserve_book(book1)
paul.take_book(book3)
john.return_book(book1)
george.take_book(book3)
george.take_book(book1)

