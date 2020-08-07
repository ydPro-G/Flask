from flask import Flask # 引入Flask包

# 创建了一个Web应用的实例'app'
app = Flask(__name__) #实例名称就是python模块名

# 定义路由规则
@app.route('/') #指明了当地址是根路径时，就调用下面的函数

# 处理请求
def index(): # 当请求地址符合路由规则时，就会进入该函数，这里是MVC的Model层
    return '<h1>Hello World!<h1>' # 在这里获取请求的request对象，返回的内容就是response


if __name__ == '__main__':
    app.run() # 启动web服务器，Web服务器默认监听本地5000端口，不支持远程访问
              # 如果想支持远程，需要在run()方法传入host=0.0.0.0 想要改变监听端口，传入post=端口号





# 注意，Flask自带的Web服务器主要还是给开发人员调试用的
# 在生产环境中，你最好是通过WSGI将Flask工程部署到类似Apache或Nginx的服务器上。