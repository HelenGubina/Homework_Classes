class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.name} {self.author}  {self.year} year"


class Library:
    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        self.books.append(book)


book1 = Book("Anna Karenina", "L. Tolstoy", 1984)
book2 = Book("Idiot", "F. Dostoyevkiy", 1976)
book3 = Book("Animal farm", "G. Orwell", 1976)

lybrary_classic = Library([])

lybrary_classic.add_book(book1)
lybrary_classic.add_book(book2)
lybrary_classic.add_book(book3)

print([str(item) for item in lybrary_classic.books])
