class Book:
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor
        self.avaible = True

    def borrow(self):
        if self.avaible:
            self.avaible = False
            print(f"EL libro {self.title} ha sido prestado")
        else:
            print(f"EL libro {self.title} no se encuentra disponible")

    def return_book(self):
        self.avaible = True
        print(f"EL libro {self.title} ha sido devuelto")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.avaible:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"EL libro {book.title} no se encuentra disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"EL libro {book.title} no esta en la lista de prestados")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_books(self, book):
        self.books.append(book)
        print(f"EL libro {book.title}, ha sido agregado")

    def register_user(self, user):
        self.users.append(user)
        print(f"EL usuario {user.name}, ha sido registrado")

    def show_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.avaible:
                print(f"{book.title}, autor {book.autor}")


book1 = Book("Programacion funcional", "James Osorio Florez")
book2 = Book("Programacion Orientada a Objectos", "Roberto Felix Jimenez")
book3 = Book("Programacion En GO", "Analuz Anorlt Suix")

user1 = User("Carolina Horthua", 1)
user2 = User("Perrito Horthua", 2)


library = Library()
library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

library.register_user(user1)
library.register_user(user2)

library.show_books()

user1.borrow_book(book1)

library.show_books()

user1.return_book(book1)

library.show_books()
