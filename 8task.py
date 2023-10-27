class Book:
    def __init__(self, name, author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    @staticmethod
    def how_many_book_in_one_year(booklist):
        dict1 ={}
        for i in booklist:
            if dict1.get(i.year) == None:
                dict1[i.year] = 1
            else:
                dict1[i.year] += 1
                
        return dict1

book1 = Book("Anna Karenina", "L. Tolstoy", 1984, 850)
book2 = Book("Idiot", "F. Dostoyevkiy", 1976, 450)
book3 = Book("Animal farm", "G. Orwell", 1976, 304)

booklist = []
booklist.append(book1)
booklist.append(book2)
booklist.append(book3)

print(Book.how_many_book_in_one_year(booklist))
