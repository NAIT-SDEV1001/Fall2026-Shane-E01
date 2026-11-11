#book class with title, author, pages, and price attributes. Use type hints
class Book:
    def __init__(self,title: str, author: str, pages: int, price: float)-> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    #override __str__ to return title by author for any book you print
    #test by instantiating a book object and printing the book
    def __str__(self)-> str:
        return f"{self.title} by {self.author}"

    #override the __eq__ method to return true if the title and author of 2 book objects are the same
    def __eq__(self, other)->bool:
        return self.title == other.title and self.author == other.author

# book1 = Book('IT','Stephen King',100,20)
# book2 = Book('IT','Stephen Kings',100,20)

# print(book1 == book2)#Book1.__eq__(book2)
# print (book1)



