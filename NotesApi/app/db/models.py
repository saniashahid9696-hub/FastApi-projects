from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .session import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    note_id = Column(Integer, ForeignKey("notes.id"))
    content = Column(Text)