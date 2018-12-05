from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

class Config(object):
    '''项目的配置'''
    DEBUG = True

    #为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/webtest"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()