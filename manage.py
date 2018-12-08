from flask import session
from flask_script import Manager                #从flask脚本中导入 管理包
from flask_migrate import Migrate, MigrateCommand  #导入数据库迁移提交库和迁移库
from App_WEB import app, db

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