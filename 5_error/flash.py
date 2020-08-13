# 消息闪现 
# 在页面上闪现一个消息
from flask import render_template,request,session,url_for,redirect,flash

@app.route('/')
def index():
    if 'user' in session:
        return render_template('hello.html',name=session['user'])
    else:
        return redirect(url_for('login'),302)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session['user'] == request.form['user']
        flash('Login successfully!') # flash消息闪现
        return redirect(url_for('index')) # 重定向到index
    else:
        return'''

        '''
# flash()方法的第二个参数是消息类型 1.message,2.info,3.warning,4.error
 # 可以在获取消息的同时获取消息类型，还可以过滤特定的消息类型，只需设置get_flashed_messages方法的with_categories和category_filter参数即可