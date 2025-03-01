from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# Creates the table and database if it does not already exist
models.Base.metadata.create_all(bind=engine)


# Everytime we open a database connection,
# we must ensure we close the connection.
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Model for a book
class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)  # 0 - 100


BOOKS = []


# Read all the books
@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Books).all()


# Create new book
@app.post("/")
def create_book(book: Book, db: Session = Depends(get_db)):
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    db.add(book_model)
    db.commit()

    return book


# Update an existing book
@app.put("/{book_id}")
def update_book(
    book_id: int,
    new_book: Book,
    db: Session = Depends(get_db),
):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:  # Gaurd clause
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id}: Does not exist.",
        )

    book_model.title = new_book.title
    book_model.author = new_book.author
    book_model.description = new_book.description
    book_model.rating = new_book.rating

    db.add(book_model)
    db.commit()

    return new_book


# Delete an existing book
@app.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} does not exist.",
        )

    db.query(models.Books).filter(models.Books.id == book_id).delete()
    db.commit()

    return {"deleted": book_model}
