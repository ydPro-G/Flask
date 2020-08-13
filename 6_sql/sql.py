# 集成数据库
# 登录的信息由数据库来验证
 # 数据库表的初始化SQL 保存在init.sql中
 # 配置文件config.py
 from flask import Flask,request,flash,redirect,url_for,render_template
import config

# 导入配置信息
app = Flask(__name__)
app.config.from_object('config')

# 建立和释放数据库连接
@app.before_request
def before_request(): # 建立数据库连接，每次请求开始时被调用，并在teardown_request()关闭它，它会在每次请求关闭前被调用
    g.db = sqlite3.connect(app.config['DATABASE']) # 数据库位置

@app.teardown_request
def teardown_request(exception):
    db = getattr(g,'db',None)
    if db is not None:
        db.close()



# 查询数据库
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['user']
        passwd = request.form['passwd']
        cursor = g.db.execute('select * from users where name=? and password=?', [name,passwd])
        if cursor.fetchone() is not None:
            session['user'] = name # 会话
            flash('login successfully!') # 消息闪烁
            return redirect(url_for('index')) # 重定向
        else:
            flash('No such user!','error') # 消息闪烁
            return redirect(url_for('login')) # 重定向
    else:
        return render_template('login.html') # 如果是post跳转到上面，反过来展示模板为login.html