
# 没有cookie，session就没法用，介绍下cookie的使用
from flask import request,session,make_response,Flask
import time

app = Flask(__name__) # 一个Web应用实例

@app.route('/login',methods=['POST','GET'])
def login():
    response = None
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            response = make_response('Admin login successfully!')
            response.set_cookie('login_time',time.strftime('%Y-%m-%d %H:%M:%S')) # 引入time模块获取当前系统时间
            # 再返回响应时，通过response.set_cookie()函数，来设置cookie项，之后这个项值会被保存到浏览器中，这个函数的第三个参数max_age可以设置该cookie项的有效期，不设的话，浏览器关闭，该Cookie失效
            ...
    else:
        if 'user' in session: 
            login_time = request.cookies.get('login_time') # 这个对象就是一个保存了浏览器Cookie的字典，使用get()可以获取相应键值
            response = make_response('Hello %s, you logged in on %s' % (session['user'],login_time))
            ...

        return response




# 全局对象g
# flask.g是Flask一个全局对象，g的作用范围就在一个请求（也就是一个线程），它不能在多个请求间共享
# 可以在g对象保存任何你想保存的内容，一个最常见的例子就是在进入请求前保存数据库链接