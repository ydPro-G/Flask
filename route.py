from flask import Flask

app = Flask(__name__)

 @app.route('/hello/<name>') # 根目录下面的hello目录，<name>是用户输入的目录，/hello/后面的参数被作为hello()函数的name参数传了进来

@ app.route('/user/<int:user_id>') # 录有类型转换器有：
                                   # 缺省：字符型，但不能有斜杠
                                   # int：整型
                                   # float: 浮点型
                                   # path: 字符型，可有斜杠
@app.route('/') # 可以有多个路由








def get_user(user_id): # 获取输入的name
    return 'User ID: %s' % user_id # user id: 你输入的数字

if __name__ == '__main__':
    app.run()