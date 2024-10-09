from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import ValidationError
from LibraryFunctions import Library, Book

app = FastAPI()
l = Library()

def send_message(message: str) -> dict:
    return { "Message" : message }

@app.get("/")
def read_root() -> RedirectResponse:
    """Sends the user to the docs, theese are automaticly generated."""
    return RedirectResponse(url="/docs")

@app.get("/all/")
def return_lib() -> dict:
    return l.get_whole_library()


@app.post("/add/")
def add_book(book:Book) -> dict:
    try:
        print(book)
        l.add_book(book.model_validate(book))
        return send_message("Book added to library!")
    except ValidationError:
        return send_message("Book failed to load onto server!")

@app.post("/delete/")
def delete_book(isbn: str) -> dict:
    if l.remove_book(isbn):
        return send_message(f"Book with ISBN: {isbn}, has been removed from the library. Much sadness.")
    else:
        return send_message(f"Could not remove book with isbn {isbn}")    
