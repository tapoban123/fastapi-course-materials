from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

# Model for a book
class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)  # 0 - 100


BOOKS = []

# Read all the books
@app.get("/")
def read_api():
    return {"books": BOOKS}

# Create new book
@app.post("/")
def create_book(book: Book):
    BOOKS.append(book)
    return book

# Update an existing book
@app.put("/{book_id}")
def update_book(book_id: UUID, new_book: Book):
    counter = 0
    for book in BOOKS:
        counter += 1
        if book.id == book_id:
            BOOKS[counter - 1] = new_book
            return BOOKS[counter - 1]

    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id}: Does not exist.",
    )

# Delete an existing book
@app.delete("/{book_id}")
def delete_book(book_id: UUID):
    counter = 0
    for book in BOOKS:
        counter += 1
        if book.id == book_id:
            del BOOKS[counter - 1]
            return f"ID: {book_id} deleted"
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} does not exist.",
    )
