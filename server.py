#!flask/bin/python
from flask import Flask, request, abort
from utils.config import config
from utils.logger import loggerWriteEvent
from app.authorization import appMiddlewareAuthentication
from app.write import appWriteEvent

port = config['flask']['port']
host = config['flask']['host']
debug = config['flask']['debug']

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@appMiddlewareAuthentication
def index():
    if request.method == 'POST':
        return appWriteEvent()
    else:
        return "TODO"


if __name__ == '__main__':
    app.run(debug=debug, host=host, port=port)
