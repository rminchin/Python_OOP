# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER, PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __book_list = None

    # TODO: create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def get_book_list():
        if Book.__book_list is None:
            Book.__book_list = []
        return Book.__book_list

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, new_title):
        self.title = new_title

    def __init__(self, title, book_type):
        self.title = title
        if book_type not in Book.BOOK_TYPES:
            raise ValueError(f"{book_type} is not a valid book type")
        else:
            self.book_type = book_type


# TODO: access the class attribute
print("Book types: ", Book.getBookTypes())

# TODO: Create some book instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "PAPERBACK")
# b3 = Book("Title 3", "COMIC")

# TODO: Use the static method to access a singleton object
the_books = Book.get_book_list()
the_books.append(b1)
the_books.append(b2)
print(the_books)
