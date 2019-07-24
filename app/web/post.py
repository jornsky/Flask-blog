from flask import render_template, redirect, request, url_for
from flask_login import login_required

from app.models.base import db
from app.models.category import Category
from app.models.post import Post
from app.models.post_category import Post_category
from . import web


#调用单蓝图多模块
@web.route("/post/<catagory>/<id>",methods=['GET','POST'])
#视图函数
def get_post():



    return render_template('post.html')


@web.route('/post/add',methods=['GET','POST'])
@login_required
def add_post():

    #get处理 显示catagory

    categorys = db.session.query(Category).all()





    content =request.form.get('ckeditor')
    if request.method == 'POST':
        # 文章页面
        post = Post()

        post.title =  request.form.get('title')
        post.content = content
        post.author = '风'
        post.create_time=1

        #文章目录关系
        # postcate = Post_category()
        # postcate.post = post
        # postcate.category = Category.query.filter_by(name=request.values.get('sel')).first()

        post.categorys.append(Category.query.filter_by(name=request.values.get('sel')).first())



        # db.session.add(postcate)

        db.session.add(post)
        db.session.commit()
        return  redirect(url_for('web.index'))


    return render_template('realpost.html',categorys = categorys)





@web.route('/post/show/<id>',methods=['GET'])
def show_post(id):
    # pid = request.args.get('id')
    pid = id
    post = Post.query.get(pid)

    if not post:
        return redirect(url_for('web.index'))


    return render_template('post.html',post=post)



