from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import models
from app.schemas.post import PostCreate
from app.api.deps import get_db

router = APIRouter()

@router.post("/")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    return db_post

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()

@router.put("/{id}")
def update_post(id: int, post: PostCreate, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).get(id)
    db_post.title = post.title
    db_post.content = post.content
    db.commit()
    return db_post

@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).get(id)
    db.delete(db_post)
    db.commit()
    return {"msg": "deleted"}