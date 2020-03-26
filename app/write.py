from flask import request
from utils.logger import loggerWriteEvent


def appWriteEvent():
    req_data = request.get_json(force=True)

    info = req_data.get('info')
    level = req_data.get('level')

    loggerWriteEvent(info, level)
    return "Log successfully written!"
