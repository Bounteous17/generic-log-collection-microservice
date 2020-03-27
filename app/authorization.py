from flask import request, abort
from functools import wraps
from utils.config import config
from utils.logger import loggerWriteEvent
from models.config import CONFIG


def appMiddlewareAuthentication(protected_resource):
    @wraps(protected_resource)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        xApiKeyRequest = request.headers.get('x-api-key')
        if xApiKeyRequest and xApiKeyRequest == CONFIG.flask.xApiKey:
            return protected_resource(*args, **kwargs)
        else:
            abort(401)
    return decorated_function
