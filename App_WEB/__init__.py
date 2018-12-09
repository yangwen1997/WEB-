from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy         #建立数据库映射关系
from redis import StrictRedis                       #从redis包中导入创建StrictRedis对象
from config import config                           #自定义session的库
from flask.ext.wtf import CSRFProtect               #导入跨站伪造保护的库
from flask_session import Session                   #导入自定义session的库


#初始化app
app = Flask(__name__)
#先初始化db对象
db = SQLAlchemy()

def  create_app(app_name):
    """创建工厂函数，根据传的参数名进行环境的切换，加载app配置信息"""

    try:
        #选择工作环境
        if app_name in config:
            app_name = config[app_name]
        else:
            print("""请根据下面的环境输入正确的环境名:
                           开发环境: development
                           生产环境: production
                           测试环境: testing""")
            string = str(input("请输入:"))
            if string in config:
                app_name = config[string]
    except:
       print("环境配置错误")

    app.config.from_object(app_name)
    #对初始化过的数据库进行和app建立映射关系
    db.init_app(app)

    #初始化redis连接
    redis_store = StrictRedis(host=app_name.REDIS_HOST, port=app_name.REDIS_PORT)

    #开启跨站伪造保护
    CSRFProtect(app)

    #指定Session，会先加载在config中配置的session信息
    Session(app)
    return app