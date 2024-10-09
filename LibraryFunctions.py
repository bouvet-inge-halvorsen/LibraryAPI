from Genre import Genre

class Book:

    def __init__(self, isbn: str, title: str, author: list, genre: Genre) -> None:
        self.ISBN = isbn
        self.title = title
        self.author = author
        self.genre = genre

    def get_book(self) -> tuple:
        return (self.ISBN, self.title, )

    def get_isbn(self) -> str:
        return self.ISBN
    
    def get_genre(self) -> list[str]:
        return self.genre
    
    def list_into_str(self, list: list) -> str:
        res: str = ""
        for author in list:
            res += author
            res += "\n"
        return res.rstrip()
    
    def pretty_print_book(self) -> dict:
        return {"ISBN":self.ISBN, "Book Title": self.title, "Authors": self.list_into_str(self.author), "Genre": self.genre.name}

class Library:
    def __init__(self) -> None:
        self.library_files: list[Book] = []
        b: Book = Book(isbn="123-123-123", title="The testing of the Tests", author=["Willie Testerson"], genre=Genre.UNKNOWN)
        self.add_book(b)

    def add_book(self, book: Book) -> bool:
        self.library_files.append(book)
        return True

    def remove_book(self, isbn) -> bool:
        for book in self.library_files:
            if book.get_isbn == isbn:
                self.library_files.remove(book)
                return True
            return False
        
    def get_whole_library(self) -> dict:
        inc = 0
        res = {}
        for book in self.library_files:
            res[inc] = book.pretty_print_book()
            inc += 1
        return res

"""This is the standard convention of telling a usaer that the file can be run as a program in it's own right"""
if __name__ == "__main__":
    l = Library()
    print(l.get_whole_library())