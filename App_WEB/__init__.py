from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy         #建立数据库映射关系
from redis import StrictRedis                       #从redis包中导入创建StrictRedis对象
from config import Config                            #自定义session的库
from flask.ext.wtf import CSRFProtect               #导入跨站伪造保护的库
from flask_session import Session                   #导入自定义session的库


#初始化app
app = Flask(__name__)

#加载app配置信息
app.config.from_object(Config)
db = SQLAlchemy(app)

#初始化redis连接
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

#开启跨站伪造保护
CSRFProtect(app)

#指定Session，会先加载在config中配置的session信息
Session(app)