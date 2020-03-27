from utils.config import config

class Flask:
    parameters = config['flask']

    def __init__(self):
        self.debug = self.parameters['debug']
        self.host = self.parameters['host']
        self.port = self.parameters['port']
        self.xApiKey = self.parameters['x-api-key']

class LoggingFileNames:
    parameters = config['logging']['fileNames']

    def __init__(self):
        self.generic = self.parameters['generic']
        self.error = self.parameters['error']

class LoggingFormat:
    parameters = config['logging']['format']

    def __init__(self):
        self.generic = self.parameters['generic']
        self.error = self.parameters['error']

class Logging:
    parameters = config['logging']

    def __init__(self):
        self.ext = self.parameters['ext']
        self.path = self.parameters['path']
        self.fileNames = LoggingFileNames()
        self.format = LoggingFormat()

class Config:
    def __init__(self):
        self.flask = Flask()
        self.logging = Logging()

CONFIG = Config()