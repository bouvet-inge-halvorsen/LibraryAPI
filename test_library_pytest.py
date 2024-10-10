import pytest
from Genre import Genre
from LibraryFunctions import Library, Book

@pytest.fixture
def book_stack() -> list:
    return [Book(ISBN="123-123-123-0", title="The testing of the Tests", author=["Willie Testerson"], genre=Genre.UNKNOWN),
            Book(ISBN="123-123-123-1", title="The testing of the Tests vol. 2", author=["Mark Testerson"], genre=Genre.UNKNOWN)]

@pytest.fixture
def library() -> Library:
    return Library()

def test_add_book(library, book_stack):
    """Tests that a book can be added to the library"""
    library.add_book(book_stack[0])

    assert library.library_files[0] == book_stack[0]

def test_can_delete_a_book(library, book_stack):
    # assert that the library is empty
    assert len(library.library_files) == 0

    # add some data to the library
    library.add_book(book_stack[0])
    library.add_book(book_stack[1])

    #assert that the data is in the library
    assert len(library.library_files) == 2