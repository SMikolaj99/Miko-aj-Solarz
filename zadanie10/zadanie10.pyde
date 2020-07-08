import unittest

class Library(): 
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook): 
        if requestedBook in self.availableBooks: 
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): 
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): 
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")

class Customer(): 
    book = "" 
    haveBook = False
    def requestBook(self, book): 
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): 
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False
        
def setup():
    size(220,100)
    global library, Madzia, Mikolaj
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Hobbit"]
    library = Library(books) 
    Madzia = Customer()
    Mikolaj = Customer()
def draw():
    library.displayAvailableBooks()
def mouseClicked(): 
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
            library.lendBook(Madzia.requestBook("Naocznosc"))
            library.lendBook(Mikolaj.requestBook("Hobbit")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
            library.addBook(Mikolaj.returnBook())        

class ZadanieDziesiate(unittest.TestCase):

    def test_wypozyczenia_2(self):
        Mikolaj = Customer()
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books)
        library.lendBook(Mikolaj.requestBook("Harry Potter"))
        self.assertEqual(["Naocznosc", "Sens Sztuki"], library.availableBooks)
        self.assertEqual(Mikolaj.book, "Harry Potter")
        self.assertTrue(Mikolaj.haveBook)

    def test_wypozyczenia_3(self):
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books)
        library.addBook("Sherlock Holmes")
        self.assertEqual(["Naocznosc", "Sens Sztuki", "Harry Potter", "Sherlock Holmes"], library.availableBooks)

if __name__ == '__main__':
    unittest.main()
    
# 2pkt
