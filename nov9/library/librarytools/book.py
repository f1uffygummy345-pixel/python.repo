class Book:
    def __init__(self, title: str, author: str, pages: int, price: float) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        
#override __str__
    def __str__(self) -> None:
        return f'{self.title} by {self.author}'
    
#when comparing objects we need to override __eq__ to define what equal means
    def __eq__(self, other:'Book')-> bool:
        return self.title == other.title


book1 = Book('a','b',5,12.0)
book2 = Book('a','b',5,12.0)

if book1 == book2:
    print("equal")