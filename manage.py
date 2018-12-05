from redis import StrictRedis           #从redis包中导入创建StrictRedis对象
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy     #建立数据库映射
from flask.ext.wtf import CSRFProtect           #跨站伪造保护

class Config(object):
    '''项目的配置'''
    DEBUG = True

    #为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/webtest"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379


app = Flask(__name__)

# 加载配置
app.config.from_object(Config)
db = SQLAlchemy(app)

# 初始化redis
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

#开启当前项目CSRF保护
CSRFProtect(app)

@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()