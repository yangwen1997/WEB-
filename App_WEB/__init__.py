import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy         #建立数据库映射关系
from redis import StrictRedis                       #从redis包中导入创建StrictRedis对象
from config import config_dict,Config               #自定义session的库
from flask_wtf.csrf import CSRFProtect               #导入跨站伪造保护的库
from flask_session import Session                   #导入自定义session的库


#初始化app
app = Flask(__name__)
#先初始化db对象
db = SQLAlchemy()

redis_store = None

def  create_app(app_name):
    """创建工厂函数，根据传的参数名进行环境的切换，加载app配置信息"""

    try:
        #选择工作环境
        if app_name in config_dict:
            app_name = config_dict[app_name]
        else:
            print("""请根据下面的环境输入正确的环境名:
                           开发环境: development
                           生产环境: production
                           测试环境: testing""")
            string = str(input("请输入:"))
            if string in config_dict:
                app_name = config_dict[string]
    except:
       print("环境配置错误")

    app.config.from_object(app_name)
    db.init_app(app)
    # 传递日志级别
    log_file(Config.LEVEL)

    #对初始化过的数据库进行和app建立映射关系





    #初始化redis连接
    global redis_store
    redis_store = StrictRedis(host=app_name.REDIS_HOST, port=app_name.REDIS_PORT)


    #开启跨站伪造保护
    CSRFProtect(app)

    #指定Session，会先加载在config中配置的session信息
    Session(app)



    # 注册蓝图
    from App_WEB.models.index import index_blu
    app.register_blueprint(index_blu)

    return app


def log_file(levels):
    """记录日志的方法 设置日志的等级"""
    logging.basicConfig(level = levels)

    #创建日志记录器、指定日志的保存位置，文件大小及个数
    file_log_handler = RotatingFileHandler("logs/log", maxBytes = 1024 * 1024 * 50, backupCount = 10)

    #创建日志记录格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s : %(lineno)s %(message)s')

    #为刚创建的日志记录器设置记录格式
    file_log_handler.setFormatter(formatter)

    #为全局的日志工具添加日志记录器
    logging.getLogger().addHandler(file_log_handler)