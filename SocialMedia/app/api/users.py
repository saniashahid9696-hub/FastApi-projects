from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import models
from app.schemas.user import UserCreate
from app.api.deps import get_db

router = APIRouter()

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).get(id)
    db.delete(user)
    db.commit()
    return {"msg": "deleted"}