from . import index_blu
from flask import session

@index_blu.route('/', methods=['GET'])
def index():
    return "第一个flask程序"