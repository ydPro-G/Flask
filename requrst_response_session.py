
# 一个完整的HTTP请求，包含客户端的Request,服务端的Response，会话Session等

# 在Flask中使用这些内建对象：request,session,cookie

# 请求对象Request
from flask import request

@ app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            return 'Admin login successfully!'
