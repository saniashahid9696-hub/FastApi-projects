from fastapi import FastAPI
from app.db.session import Base, engine
from app.api import users, posts, comments, likes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users")
app.include_router(posts.router, prefix="/posts")
app.include_router(comments.router, prefix="/comments")
app.include_router(likes.router, prefix="/likes")