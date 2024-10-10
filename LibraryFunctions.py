from pydantic import BaseModel, Field
from Genre import Genre

class Book(BaseModel):
    ISBN: str = Field(...,description="The International Standard Book Number that is intended to be unique.", min_length=10, max_length=13)
    title: str = Field(..., min_length=1)
    author: list[str] = Field(..., min_length=1)
    genre: Genre = Field(default=Genre.UNKNOWN)

    def __init__(self, ISBN: str, title: str, author: list, genre: Genre = Genre.UNKNOWN) -> None:
        super().__init__(ISBN = ISBN, title = title, author= author, genre = genre)

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

    def add_book(self, book: Book) -> bool:
        self.library_files.append(book)
        return True

    def remove_book(self, isbn:str) -> bool:
        acc = 0
        for book in self.library_files:
            if book.get_isbn() == isbn:
                self.library_files.pop(acc)
                return True
            acc+=1
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