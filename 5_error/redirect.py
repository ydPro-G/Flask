# 重定向

# 当客户端浏览某个网址时，将其导向到另一个网址（用户未登录时将其重定向到登录页要求其登录
from flask import session,redirect,Flask,url_for # 会话,重定向

app = Flask(__name__)

@app.route('/')
def index():
    if 'user' in session:
        return 'Hello %s' % session['user']
    else:
        return redirect(url_for('login'),302) # redirect 重定向，第二个参数是HTTP状态码，302暂时重定向，304 返回状态码