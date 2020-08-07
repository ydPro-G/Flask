# HTTP请求方法设置，Get,Post,Put,Delete
from flask import request
from flask import Flask
app = Flask(__name__)
@app.route('/login',methods=['GET','POST'])

def login():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'

if __name__ == '__main__':
    app.run()