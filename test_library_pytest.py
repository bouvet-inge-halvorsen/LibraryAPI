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
    assert library.add_book(book_stack[0]) == True

    assert library.library_files[0] == book_stack[0]

#TODO: should be moved to tests for books or something
def test_can_get_isbn_from_book(book_stack):
    assert book_stack[0].get_isbn() == "123-123-123-0"

def test_can_delete_a_book(library, book_stack):
    # assert that the library is empty
    assert len(library.library_files) == 0

    # add some data to the library
    library.add_book(book_stack[0])
    library.add_book(book_stack[1])

    # assert that the data is in the library
    assert len(library.library_files) == 2

    # removing a book will return a bool, true if book was removed
    assert library.remove_book(book_stack[0].get_isbn()) == True
    
    # with the book deleted, teher should be 1 book left
    assert len(library.library_files) == 1

    # and there should be no possibility to delete the prevous book
    assert library.remove_book(book_stack[0].get_isbn()) == False

def test_should_not_be_able_to_add_a_book_that_already_exists(library, book_stack):
    # assert that the library is empty
    assert len(library.library_files) == 0

    # add a book to the library
    assert library.add_book(book_stack[0]) == True

    # assert that the book is in the library
    assert library.get_whole_library()[0] == book_stack[0].pretty_print_book()

    # If the book exists, return False
    assert library.add_book(book_stack[0]) == False