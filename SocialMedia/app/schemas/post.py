from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
    owner_id: int

class PostOut(PostCreate):
    id: int

    class Config:
        from_attributes = True