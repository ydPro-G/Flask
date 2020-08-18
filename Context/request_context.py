

# 请求上下文的生命周期

 #   上下文装饰器[@app.before_request]和[@app.teardown_request]，用其修饰的函数称为上下文Hook函数
 #   flask还提供了装饰器@app.after_request
 #   before_request 修饰的函数会在请求处理之前被调用
 #   after_request和taerdown_request在请求处理完成后被调用

 #   after_request只会在请求正常退出时才会被调用，它传入一个参数接受响应对象，并返回一个响应对象，一般用来统一修改响应的内容
 #   teardown_request在任何情况下都会被调用，传入一个参数来接受异常对象，一般用来统一释放请求所占有的资源。
 #   同一种类型的HOOk函数可以存在多个，程序会按照代码中的顺序执行

from flask import Flask,g,request

app = Flask(__name__)

@app.before_request
def before_request():
    print('before request started')
    print(request.url)


@app.before_request
def before_request2():
    print('before request started 2')
    print(request.url)
    g.name = 'SampleApp'

@app.after_request
def after_request(response):
    print('after request finfished')
    print(request.url)
    response.headers['key'] = 'value'
    return response

@app.teardown_request
def teardown_request(exception):
    print('teardown request')
    print(request.url)

@app.route('/')
def index():
    return 'Hello, %s!' % g.name

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

