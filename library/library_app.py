from library_tools.book import Book
from library_tools.library import Library

def main():
    library1 = Library("Good Books")
    print(library1)
    library1.add_book(Book("Hunger Games","Suzanne Colins",400,20))
    library1.add_book(Book("Catching Fire","Suzanne Colins",400,20))
    library1.list_books()
    search_result = library1.find_book("Catching Fire")
    if search_result is None:
        print("Book not found!")
    else:
        print (f"Book found: {search_result}")        

if __name__ == "__main__":
    main()