class Book:
    def __init__(self,book_name:str,book_price:int) -> None:
        self.book_name = book_name
        self.book_price = book_price

    def __add__(self,other):
        total = self.book_price+other.book_price
        return total

##Creating the instance for each object
t1 = Book("Hello mr",500)
t2 = Book("Jackson",600)
t3 = Book("C++ Programming Concept",800)

print(f"Total of two oject is {t1+t2}")