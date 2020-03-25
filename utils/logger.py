from logging import basicConfig, info, INFO
from utils.config import config

filename = config['logging']['filename']
logFormat = config['logging']['format']['info']

basicConfig(filename=filename, filemode='w', format=logFormat, level=INFO)

def writeInfoLog(message):
    info(message)