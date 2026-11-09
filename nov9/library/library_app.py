from librarytools.library import Library
from librarytools.book import Book


def main():
    library = Library("Not a library")
    print(library)
    
    library.list_books()
    library.add_book(Book('a','b',500,12.0))
    library.add_book(Book('c','d',1200,1200))
    library.add_book(Book('s','w',200,120))
    library.list_books()
    
    
    result = library.find_book('c')
    
if __name__ == '__main__':
    main()