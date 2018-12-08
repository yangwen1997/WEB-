from redis import StrictRedis           #从redis包中导入创建StrictRedis对象
from flask import Flask,session
from flask.ext.sqlalchemy import SQLAlchemy     #建立数据库映射
from flask.ext.wtf import CSRFProtect           #跨站伪造保护
from flask_session import Session               #自定义session的库
from flask_script import Manager                #从flask脚本中导入 管理包
from flask_migrate import Migrate, MigrateCommand  #导入数据库迁移提交库和迁移库

class Config(object):
    '''项目的配置'''
    DEBUG = True
    #设置启动模式秘钥
    SECRET_KEY = 'adO9TUW0KoxTuG+wstHqD59hvJAOexP6bIUROcrityGAdaSxkOvbKRIVdpcyttk1'

    #为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/webtest"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    #对Session进行配置
    '''SESSION_TYPE : session的存贮类型  SESSION_REDIS：redis的ip端口 
       SESSION_USE_SIGNER : 是否开启签名 SESSION_PERMANENT :是否永久保存
       PERMANENT_SESSION_LIFETIME : session的过期时间    
    '''
    SESSION_TYPE = "redis"
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port= REDIS_PORT)
    SESSION_USE_SIGNER = True
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 84000 * 2

app = Flask(__name__)

# 加载配置
app.config.from_object(Config)
db = SQLAlchemy(app)

# 初始化redis
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

#开启当前项目CSRF保护
CSRFProtect(app)
#指定Session
Session(app)
#管理app
manger = Manager(app)
#进行数据库和app的迁移关联操作
Migrate(app, db)
#提交迁移操作
manger.add_command('db', MigrateCommand)

@app.route('/')
def index():
    session["name"] = 'flask'
    return 'index'


if __name__ == '__main__':
    manger.run()