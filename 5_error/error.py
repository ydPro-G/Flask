from flask import abort,Flask
app = Flask(__name__)

@app.route('/error')
def error():
    abort(404) # abort 异常终止，限时浏览器404错误页面



# 重写错误页面
@app.errorhandler(404) # 装饰器
def page_not_found(error): # 调用page_not_found()函数
    return render_template('404.html')# 404返回404.html模板页，第二个参数代表错误代码


# 自定义一个异常
class InvalidUsage(Exception): # 无效用法：异常
    status_code = 400
    def __init__(self,message,status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code


@app.errorhandler(InvalidUsage) # 通过装饰器修饰函数invalid_usage()
def invalid_usage(error): # 一旦遇到InvalidUsage异常被抛出，这个invalid_usage()函数就会被调用
    response = make_response(error.message)
    response.status_code = error.status_code 
    return response