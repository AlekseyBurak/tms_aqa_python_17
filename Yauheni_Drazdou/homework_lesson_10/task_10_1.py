class Books:

    def __init__(self, bookname: str, author: str, pages: int, year: int, serial: int,
                 avail: True):
        """
    This function show parameters for objects in class Books
        :param bookname: 
        :param author: 
        :param pages: 
        :param year: 
        :param serial: protected inventory number
        :param avail: shows if the book is available at present moment
        """
        self.bookname = bookname
        self.author = author
        self.pages = pages
        self.year = year
        self.__serial = serial
        self.avail = avail

    def __str__(self):
        if self.avail is True:
            return f"{self.bookname}, {self.author}, {self.year}, available"
        else:
            return f"{self.bookname}, {self.author}, {self.year}, not available"

    @property
    def serial(self):
        return self.__serial

    @serial.deleter
    def serial(self):
        self.__serial = 0



nineteen_eighty_four = Books("1984", "George Orwell", 720, 2022,
                             123456, True)
stihi_bikova = Books("Стихи Василя Быкова", "Василь Быков", 176, 2002,
                     123457, True)
mast_and_marg = Books("Мастер и Маргарита", "Михаил Булгаков", 512, 2024,
                      123458, True)

print(nineteen_eighty_four)
print(stihi_bikova)
print(mast_and_marg)

class Readers:

    def __init__(self, name: str, dob: int, read=None):
        """
        This function gives arguments to objects in class Readers 
        :param name: reader's name
        :param dob: reader's date of birth
        :param read: names of books the reader took or reserved
        """
        self.name = name
        self.dob = dob
        if read is None:
            read = []
        self.read = read

    def __str__(self):
        """
        :return: name of objects and the books that are attached to the reader
        """
        return f"{self.name}, {self.read}"

    def make_res(self, other):
        """
    This function allows reader to reserve a book if it's available
        :param other: marks book unavailable for other users
        :return: adds book to readers list
        """
        if other.avail is False:
            print(f"Sorry, {self.name}, '{other.bookname}' is not available at this moment")
        else:
            self.read.append(other.bookname)
            print(f"{self.name}, '{other.bookname}' is reserved")
            other.avail = False

    def cancel_res(self, other):
        """
        This function cancels book's reservation
        :param other: makes a book available
        :return: removes the book from readers list
        """
        print("Reservation is canceled, thank you")
        other.avail = True
        self.read.remove(other.bookname)

    def take_book(self, other):
        """
            This function allows reader to take a book if it's available
                :param other: marks a book unavailable for other readers
                :return: add book to reader's list
                """
        if other.avail is False:
            print(f"Sorry, {self.name}, '{other.bookname}' is not available at this moment")
        else:
            self.read.append(other.bookname)
            print(f"Here is your book, {self.name}")
            other.avail = False

    def return_book(self, other):
        """
        This function returns a book
        :param other: makes book available for othe readers
        :return: removes the book from readers list
        """
        print(f"Thank you, for returning the book '{other.bookname}', {self.name}")
        other.avail = True
        self.read.remove(other.bookname)

nick = Readers("Ник", 1988, None)
mike = Readers("Майк", 1999, None)
alex = Readers("Саша", 1954, None)

alex.make_res(stihi_bikova)
print(stihi_bikova)
print(alex)

mike.make_res(stihi_bikova)
print(stihi_bikova)
print(mike)

alex.return_book(stihi_bikova)
print(stihi_bikova)
print(alex)

mike.make_res(stihi_bikova)
print(stihi_bikova)
print(mike)

nick.take_book(nineteen_eighty_four)
nick.take_book(mast_and_marg)
nick.make_res(stihi_bikova)
print(nineteen_eighty_four)
print(mast_and_marg)
print(nick)

nick.return_book(nineteen_eighty_four)
print(nineteen_eighty_four)
print(nick)