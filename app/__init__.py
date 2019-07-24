"""
python模块的初始化文件夹
以及Flask的初始化文件 定义了模板位置，静态文件的存放位置
"""
from flask import Flask
from app.models.base import db
from flask_login import  LoginManager
from flask_ckeditor import CKEditor

#富文本编辑器
ckeditor = CKEditor()
login_manager = LoginManager()
def create_app():
    app = Flask(__name__,template_folder='templates',static_folder='static')
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    #注册模块蓝图
    register_web_blueprint(app)


    #注册数据库

    db.init_app(app)
    db.create_all(app=app)

    #初始化login
    login_manager.init_app(app)
    #初始化登入野页面
    login_manager.login_view='web.login'
    login_manager.login_message_category='warning'
    login_manager.login_message=u'请先登入！'

    ckeditor.init_app(app)


    return app


#蓝图和app绑定
def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

