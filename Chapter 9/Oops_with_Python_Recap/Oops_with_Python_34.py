class Library:
    def __init__(self,name) -> None:
        self.name = name
        self.books = []
    
    class Book:
        def __init__(self,Author,Bookname) -> None:
            self.Author = Author
            self.Bookname = Bookname
        
        def display_info(self):
            return f"Title {self.Author} and {self.Bookname}"
        
    def addbook(self,authorname,bookname):
        new_book = self.Book(authorname,bookname)
        self.books.append(new_book)
    
    def display_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            print(book.display_info())

# Usage of the classes
if __name__ == "__main__":
    library = Library("City Library")
    
    # Adding books to the library
    library.addbook("To Kill a Mockingbird", "Harper Lee")
    library.addbook("1984", "George Orwell")
    
    # Displaying books
    library.display_books()