from flask import Flask
from flask import render_template # 提供标题
# 实例化一个Web应用
app  = Flask(__name__)

@app.route('/hello') # 路由
@app.route('/hello/<name>') # 路由


# 路由函数
def hello(name=None): # hello函数并不是直接返回字符串，而是调用render_template()方法渲染模板
    return render_template('hello.html',name=name) # hello.html指向想要渲染的模板名称，第二个参数就时想要传到模板的变量，变量可以传多个


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


# html 不能加注释
# 根据name的值来显示不同内容
# 变量或表达式用{{}}修饰
# 控制语句用{% %}修饰


# 模板继承
 # 虽然render_template()加载的是hrllo.html模板，但是layout.html的内容也被一起加载了
 # hello.html中的内容被放到了layout.html中{% block body %}的位置上hello继承了layout


 # html 自动转义