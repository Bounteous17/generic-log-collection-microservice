#!flask/bin/python
from flask import Flask, request, abort
from models.config import CONFIG
from utils.logger import loggerWriteEvent
from app.authorization import appMiddlewareAuthentication
from app.write import appWriteEvent

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@appMiddlewareAuthentication
def index():
    if request.method == 'POST':
        return appWriteEvent()
    else:
        return "TODO"


if __name__ == '__main__':
    app.run(
        debug=CONFIG.flask.debug,
        host=CONFIG.flask.host,
        port=CONFIG.flask.port
    )
