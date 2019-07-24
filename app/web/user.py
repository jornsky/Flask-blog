from flask import render_template, request, flash, url_for, redirect
from flask_login import login_user

from app.models.base import db
from app.models.user import User
from . import web


#对返回页面和用户提交方式的不同分别写代码
@web.route('/register',methods=['GET','POST'])
def register():
    form = request.form
    if request.method == 'POST':
        user = User()
        user.set_attrs(form)
        db.session.add(user)
        db.session.commit()




    return  render_template('register.html')

@web.route('/login',methods=['GET','POST'])
def login():
    form = request.form
    if request.method== 'POST':
        user = User.query.filter_by(email=form['email']).first()
        if user and user.check_password(form['password']):
            login_user(user)  #写入Cookie 通过模型类继承



            print('密码正确！')
            # return  redirect(url_for('web.add_post'))
            next = request.args.get('next')
            print(next)
            if not next or not next.startswith('/'):
                next = url_for('web.index')


            return redirect(next)


        else:
            flash("账户不存在或者密码错误！")
            print("密码错误")

    return render_template('login.html')




