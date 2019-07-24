from flask import render_template

from app.models.base import db
from app.models.post import Post
from . import web




@web.route('/')
def index():
    #查询数据库Post表返回所有数据
    all =  db.session.query(Post).all()
    return render_template('index.html',data=all)

