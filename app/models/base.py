from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer

db = SQLAlchemy()

# 定义多对多2张表的关系
# post_category = db.Table('post_category',
#                         db.Column('post_id',db.Integer,db.ForeignKey('post.id'),primary_key=True),
#                         db.Column('category_id',db.Integer,db.ForeignKey('category.id'),primary_key=True)
#
# )


class Base(db.Model):
    #不创建这个表 作为基类
    __abstract__ = True
    create_time = Column('create_time',Integer)

#为对象动态赋值
    def set_attrs(self,attrs_dict):
        for k,v  in attrs_dict.items():
           if hasattr(self,k) and k!='id':
               setattr(self,k,v)



