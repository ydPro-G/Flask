
# 会话可以用来保存当前请求的一些状态，以便在请求之前共享信息
from flask import request,session,Flask
app = Flask(__name__)

@app.route('/login',methods=['POST','GET']) # 路由规则 与请求方式
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':   # from变量是一个字典，可以获取Post请求表单中的内容
            session['user'] = request.form['user']
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return 'Hello %s!' % session['user']
    else:
        title = request.args.get('title','Default') # 获取参数：获取GET请求中URL的参数，第二个参数是默认值，当url参数不存在时，返回默认值
        return render_template('login.html',title=title) # 提供模板
    app.secret_key = '123456' # 使用session时要设置密钥

def logout(): # 登出：清除字典的键值
    session.pop('user',None)
    return redirect(url_for('login'))