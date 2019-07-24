from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.models.base import  Base


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nicename = Column(String(50),nullable=False)
    email = Column(String(100),nullable=False)
    _password = Column('password',String(128))
    create_time = Column(String(100))
    status = Column(SmallInteger,default=0)
    counts = Column(Integer,default=0)

    #属性的读取和写入 getter setter 预处理
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)


    def check_password(self,raw):
        return  check_password_hash(self._password,raw)

# usr Modele继承UserMxxin 和这个注解 就可以使用curret_user
@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))









