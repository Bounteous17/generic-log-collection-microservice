from models.logger import LoggerLevel
from models.config import CONFIG
from utils.config import config
from logging import DEBUG, WARN, ERROR, FATAL
from logging import basicConfig, info, debug, warn, error, fatal


def setBasicConfig(filename: str, filemode: str, format: str, level: int):
    basicConfig(
        filename=filename,
        filemode=filemode,
        format=format,
        level=level
    )


def getLevel(level: LoggerLevel):
    switcher = {
        LoggerLevel.DEBUG.name: {
            "level": DEBUG,
            "severity": debug
        },
        LoggerLevel.WARN.name: {
            "level": WARN,
            "severity": warn
        },
        LoggerLevel.ERROR.name: {
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
    filemode: str = 'a'

    setBasicConfig(
        CONFIG.logging.fileNames.generic,
        filemode,
        CONFIG.logging.format.generic,
        loggerBasicConfig['level']
    )

    severity = loggerBasicConfig['severity']
    severity(info)
