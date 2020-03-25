#!flask/bin/python
from flask import Flask, request, abort
from functools import wraps
from utils.config import config
from utils.logger import writeInfoLog

port = config['flask']['port']
host = config['flask']['host']
debug = config['flask']['debug']
xApiKey = config['flask']['x-api-key']

app = Flask(__name__)


def require_xApiKey(protected_function):
    @wraps(protected_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        xApiKeyRequest = request.headers.get('x-api-key')
        if xApiKeyRequest and xApiKeyRequest == xApiKey:
            return protected_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function


@app.route('/', methods=['GET', 'POST'])
@require_xApiKey
def index():
    if request.method == 'POST':
        req_data = request.get_json(force=True)
        message = req_data.get('message')
        writeInfoLog(message)
        return "Log successfully written!"
    else:
        return "TODO"


if __name__ == '__main__':
    app.run(debug=debug, host=host, port=port)
