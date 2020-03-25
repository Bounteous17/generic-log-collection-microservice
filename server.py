#!flask/bin/python
from flask import Flask, request, abort
from functools import wraps
from utils.config import config

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
        print(xApiKeyRequest)
        if xApiKeyRequest and xApiKeyRequest == xApiKey:
            return protected_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function


@app.route('/')
@require_xApiKey
def index():
    return "Log successfully written!"


if __name__ == '__main__':
    app.run(debug=debug, host=host, port=port)
