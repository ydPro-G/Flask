# Flask提供了logger对象
from flask import session,Flask

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

app = Flask(__name__)

@app.route('/exception')
def exception():
    app.logger.debug('Enter exception method') 
    app.logger.error('403 errpr happened') 
    raise InvalidUsage('No privilege to access the resource',status_code=403)

server_log = TimedRotatingFileHandler('server.log','D')# 记录所有级别的日志
server_log.setLevel(logging.DEBUG)
server_log.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

error_log = TimedRotatingFileHandler('error.log', 'D')# 只记录错误日志
error_log.setLevel(logging.ERROR)
error_log.setFormatter(logging.Formatter('%(asctime)s: %(message)s [in %(pathname)s:%(lineno)d]'))

app.logger.addHandler(server_log)
app.logger.addHandler(error_log)