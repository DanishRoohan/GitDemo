import inspect
import logging


class logger:
    @staticmethod
    def getlogger():
        logs = inspect.stack()[1][3]
        log_name = logging.getLogger(logs)
        log_fileHandler = logging.FileHandler("Log/LogsReport.log")
        log_Formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        log_fileHandler.setFormatter(log_Formatter)
        log_name.addHandler(log_fileHandler)
        log_name.setLevel(logging.DEBUG)
        return log_name

