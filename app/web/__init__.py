from flask import Blueprint

web = Blueprint('web',__name__)

#导入需要蓝图的Controller模块 否则不会执行
from app.web import post

from app.web import index
from app.web import category
from app.web import user



