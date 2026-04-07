from sqlalchemy import Column, Integer, String, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from .session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    posts = relationship("Post", back_populates="owner", cascade="all, delete")
    comments = relationship("Comment", cascade="all, delete")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")
    comments = relationship("Comment", cascade="all, delete")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    content = Column(Text)

    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    post_id = Column(Integer)

    __table_args__ = (UniqueConstraint('user_id', 'post_id'),)