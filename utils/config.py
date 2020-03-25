import json
from distutils.util import strtobool

def getConfig():
    with open('./config.json') as json_data_file:
        data = json.load(json_data_file)
    data['flask']['debug'] = strtobool(data['flask']['debug'])
    return data

config = getConfig()