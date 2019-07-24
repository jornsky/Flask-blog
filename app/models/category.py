from sqlalchemy import Integer, String,Column
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.models.post_category import Post_category


class Category(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50),nullable=False,unique=True)

    #反向调用  post.categorys.append(<class(Category)>) secondary 关系表
    posts = relationship('Post', secondary=Post_category.__table__,
                             backref=db.backref('categorys', lazy='dynamic'))





