from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


#多对多的关系表 关联user和post表
class Post_category(Base):

    id = Column(Integer, primary_key=True, autoincrement=True)
    post = relationship('Post')
    pid = Column(Integer,ForeignKey('post.id'))

    category = relationship('Category')
    cid = Column(Integer,ForeignKey('category.id'))



