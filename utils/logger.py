from models.logger import LoggerLevel
from utils.config import config
from logging import DEBUG, WARN, ERROR, FATAL
from logging import basicConfig, info, debug, warn, error, fatal


filename = config['logging']['filenames']['generic']
genericFormat = config['logging']['format']['generic']


def setBasicConfig(filename: str, filemode: str, format: str, level: int):
    basicConfig(filename=filename, filemode=filemode,
                format=format, level=level)


def getLevel(level: LoggerLevel):
    switcher = {
        LoggerLevel.DEBUG: {
            "level": DEBUG,
            "severity": debug
        },
        LoggerLevel.WARN: {
            "level": WARN,
            "severity": warn
        },
        LoggerLevel.ERROR: {
            "level": ERROR,
            "severity": error
        }
    }
    return switcher.get(level, {
        "level": FATAL,
        "severity": fatal
    })


def loggerWriteEvent(info: str, level: LoggerLevel):
    loggerBasicConfig = getLevel(level)

    setBasicConfig(
        filename,
        'w',
        format=genericFormat,
        level=loggerBasicConfig['level']
    )

    severity = loggerBasicConfig['severity']
    severity(info)
