from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import models
from app.schemas.comment import CommentCreate
from app.api.deps import get_db

router = APIRouter()

@router.post("/")
def add_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    return db_comment