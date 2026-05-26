""" Write a Python program that implements a Library Management System using OOP.
The program should:
  - Define a Book class with title, author, and availability status
  - Define a Library class that stores multiple books (has-a relationship)
Allow:
  - adding books
  - removing books
  - borrowing books
  - returning books
  - displaying all books
  - displaying only available books
Use a menu-driven interface
Handle invalid input using try/except. """

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print("Book successfully borrowed!")
        else:
            print("Book is already borrowed!")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print("Book successfully returned!")
        else:
            print("Book is already available!")

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"Title: {self.title} | Author: {self.author} | Status: {status}"


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        if self.find_book(book.title):
            print("Book already exists in the library!")
        else:
            self.__books.append(book)
            print("Book added successfully!")

    def remove_book(self, book):
        if book is None:
            print("Book not found in library!")
        else:
            self.__books.remove(book)
            print("Book removed successfully!")

    def find_book(self, title):
        for book in self.__books:
            if book.title == title:
                return book
        return None

    def show_all(self):
        if not self.__books:
            print("No books available")
            return

        print("\nBooks list:")
        for book in self.__books:
            print(book)

    def show_available(self):
        if not self.__books:
            print("No books available")
            return

        print("\nAvailable books:")
        for book in self.__books:
            if book.is_available:
                print(book)


def main():
    library = Library()

    while True:
        try:
            print("\nLIBRARY MANAGEMENT MENU")
            print("\n1. Add book")
            print("2. Remove book")
            print("3. Borrow book")
            print("4. Return book")
            print("5. Show all books")
            print("6. Show available books")
            print("7. Exit")

            option = int(input("Choose option: "))

            if option == 1:
                title = input("Title: ")
                author = input("Author: ")
                book = Book(title, author)
                library.add_book(book)

            if option == 2:
                title = input("Title: ")
                book = library.find_book(title)
                library.remove_book(book)

            if option == 3:
                title = input("Title: ")
                book = library.find_book(title)

                if book is None:
                    print("Book not found!")
                else:
                    book.borrow()

            if option == 4:
                title = input("Title: ")
                book = library.find_book(title)

                if book is None:
                    print("Book not found!")
                else:
                    book.return_book()

            if option == 5:
                library.show_all()

            if option == 6:
                library.show_available()

            if option == 7:
                print("Exit")
                break

        except ValueError:
            print("Invalid input!")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()


