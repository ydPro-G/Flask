
# 一个完整的HTTP请求，包含客户端的Request,服务端的Response，会话Session等

# 在Flask中使用这些内建对象：request,session,cookie

# 请求对象Request
from flask import request
from flask import Flask
app = Flask(__name__)

@ app.route('/login',methods=['POST','GET'])  
def login():
    if request.method == 'POST': # request中的method变量可以获取当前请求的方法
        if request.form['user'] == 'admin':  # from变量是一个字典，可以获取Post请求表单中的内容
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    title = request.args.get('title','Default') # 获取get请求url中的参数，该函数的第二个参数是默认值，当url不存在时，则返回默认值
    return render_template('login.html',title=title)

if __name__ == '__main__':
    app.run()


    