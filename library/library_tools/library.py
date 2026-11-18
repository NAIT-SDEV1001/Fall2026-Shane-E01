#import Book 
from .book import Book

# library class with name and books[] attributes
# name will be a parameter in the constructor
# books will be initialized to an empty list
class Library:
    def __init__(self,name: str)-> None:
        self.name = name
        self.books = []

    #create a str override to return the name of the library
    def __str__(self)-> str:
        return self.name

    #method to add a book to the books list
    #It will have a book parameter(book object)
    def add_book(self, book: Book)->None:
        self.books.append(book)

    #list_books method. List all books format-> title by author
    #if there are no books in the library print"no books in library"
    def list_books(self)->None:
        print("Books in library:")
        if not self.books:#if list is empty
            print("No books in library")
        else:
            for book in self.books:
                print(book)

    #method to search for a book by its title
    #if found, return that book object
    #otherwise return None
    def find_book(self, title: str)->Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None


