
# 构建响应：先构建响应对象，设置一些参数，再将其返回
from flask import request,session,make_response,Flask

app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        ...
        if 'user' in session:
        ...
    else:
        title = request.args.get('title','Default')
        # make_response用来构建response对象，第二个参数代表响应状态码，缺省就是200
        response = make_response(render_template('login.html',title=title),200)
        response.headers['key'] = 'value'
        return response