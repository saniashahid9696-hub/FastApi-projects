from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db import models
from app.schemas.notes import NoteCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = models.Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.get("/")
def get_notes(db: Session = Depends(get_db)):
    return db.query(models.Note).all()