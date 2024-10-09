from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import LibraryFunctions

app = FastAPI()

@app.get("/")
def read_root() -> dict:
    return RedirectResponse(url="/docs")

@app.get("/all")
def return_lib() -> dict:
    l = LibraryFunctions.Library()
    return l.get_whole_library()

