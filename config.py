from redis import StrictRedis


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