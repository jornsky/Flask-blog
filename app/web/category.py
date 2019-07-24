from flask import render_template, redirect, url_for

from app.models.base import db
from app.models.category import Category
from app.models.post import Post
from app.models.post_category import Post_category
from . import web





@web.route('/category/add/<name>')

def add_category(name):
    cate = Category(name=name)
    cate.create_time=1
    db.session.add(cate)
    result = db.session.commit()

    return  redirect(url_for('index'))



@web.route('/category/<name>',endpoint='category',methods=['GET'])
def category_show_post(name):
    category = Category.query.filter_by(name=name).first()
    p_cs = Post_category.query.filter_by(cid =category.id).all()

    pids = []

    for p_c in  p_cs:
        pids.append(p_c.pid)
    print(pids)
    # mysql in
    posts = Post.query.filter(Post.id.in_(pids)).all()



    return render_template('category.html',data= posts)



