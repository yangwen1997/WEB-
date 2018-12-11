from . import index_blu
from flask import session
from App_WEB import redis_store

@index_blu.route('/', methods=['GET'])
def index():
    redis_store.set("name",'杨文龙')
    a = redis_store.get("name")
    return a