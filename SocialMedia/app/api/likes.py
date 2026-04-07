from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import models
from app.api.deps import get_db

router = APIRouter()

@router.post("/")
def like_post(user_id: int, post_id: int, db: Session = Depends(get_db)):
    like = models.Like(user_id=user_id, post_id=post_id)
    db.add(like)
    db.commit()
    return {"msg": "liked"}

@router.delete("/")
def unlike_post(user_id: int, post_id: int, db: Session = Depends(get_db)):
    like = db.query(models.Like).filter_by(user_id=user_id, post_id=post_id).first()
    db.delete(like)
    db.commit()
    return {"msg": "unliked"}