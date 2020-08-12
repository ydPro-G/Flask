# HTTP请求方法设置，Get,Post,Put,Delete
from flask import request
from flask import Flask

# 创建Web应用实例
app = Flask(__name__)

# 指定路由与HTTP请求方法，不同的请求方法可以返回不同的数据
@app.route('/login',methods=['GET','POST'])

# 路由函数
def login():
    # 请求路由为什么就反什么数据
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'

# 启动 Web服务器
if __name__ == '__main__':
    app.run()




# 2.URL构建方法
 # Flask提供了【url_for()】方法来快速获取及构建URL，方法第一个参数指向函数名（被@app.route注解的函数），
 # 后续的参数对应要构建的URL变量
url_for('login') # 返回/login

url_for('login',id='1') # 将id作为URL参数，返回/login?id=1

url_for('hello',name='man')  # 适配hello函数的name参数 返回/hello/man

url_for('static') # 获取静态文件目录
url_for('static',filename='style.css') # 静态文件地址，返回/static/style.css






#3. 静态文件位置
# 一个web应用的静态文件包括了JS，CSS，图片等，将所有文件放进static子目录中
# 使用url_for('static')来获取静态文件目录
# 改变静态目录位置;
app = Flask(__name__, static_folder='files')