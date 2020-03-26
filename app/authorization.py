from flask import request, abort
from functools import wraps
from utils.config import config

xApiKey = config['flask']['x-api-key']


def appMiddlewareAuthentication(protected_resource):
    @wraps(protected_resource)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        xApiKeyRequest = request.headers.get('x-api-key')
        if xApiKeyRequest and xApiKeyRequest == xApiKey:
            return protected_resource(*args, **kwargs)
        else:
            abort(401)
    return decorated_function
