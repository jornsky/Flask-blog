from sqlalchemy import Column, String, Integer, SmallInteger
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.models.post_category import Post_category


class Post(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(30),nullable=False)
    title = Column(String(200),nullable=False)
    content = Column(String(1000),nullable=False)









