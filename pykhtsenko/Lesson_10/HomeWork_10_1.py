class Book:
    def __init__(self, name: str, author: str, pages: int, IBN: int, reserve: bool, flag: bool):
        '''
             name - название книги
             author - автор книги
             pages - количество страниц
             IBN - инвентарный номер
             reserve - резервация книги
             flag - на руках книга или свободна
        '''

        self.name = name
        self.author = author
        self.pages = pages
        self.IBN = IBN
        self.reserve = reserve
        self.flag = flag

    def __str__(self):
        return f"This is book {self.name}. Number of the pages: {self.pages}"

# изменение статуса резервирования
    def change_reserve(self, status: bool):
    	if self.reserve and status:
    		raise ValueError("Книга зарезервирована")
    	self.reserve = status

    def change_status(self, status: bool):
    	if self.flag and status:
    		raise ValueError("Книга занята")
    	self.flag = status


book1 = Book("Tom and Jeery", "Tom Cruse", "35", "3654123", "True", "False")
print(book1)


class User:

	my_books = {}

	def __init__(name: str, last_name: str, number: int):
		self.name = name
		self.last_name = last_name
		self.number = number

	def get_book(self, book: Book):
		if book.IBN in self.my_books:
			raise ValueError("Книга уже у вас")
		book.change_status(True)
		self.my_books.add(book.IBN)

	def return_book(self, book: Book):
		if not (book.flag and book.IBN in self.my_books):
			raise ValueError("Не наша книга")
		book.change_status(False)
		my_books.remove(book.IBN)

	def reserve_book(self, book: Book):
			if book.reserve is True:
				raise ValueError("Книга уже зарезервирована")
			book.change_status(False)
#### доработать