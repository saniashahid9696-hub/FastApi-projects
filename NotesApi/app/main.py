from fastapi import FastAPI
from app.api import notes, chat
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(notes.router, prefix="/notes")
app.include_router(chat.router)