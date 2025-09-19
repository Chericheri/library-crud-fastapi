from sqlalchemy.orm import Session
import models, schemas

# ----- Authors -----
def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author); db.commit(); db.refresh(db_author)
    return db_author

def delete_author(db: Session, author_id: int):
    db.query(models.Author).filter(models.Author.id == author_id).delete()
    db.commit()

# ----- Books -----
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book); db.commit(); db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, title: str):
    db_book = get_book(db, book_id)
    if db_book:
        db_book.title = title
        db.commit()
    return db_book

def delete_book(db: Session, book_id: int):
    db.query(models.Book).filter(models.Book.id == book_id).delete()
    db.commit()