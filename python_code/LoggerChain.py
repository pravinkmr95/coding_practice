from abc import ABC, abstractmethod
from enum import Enum, auto


class LogLevel(Enum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()


class Logger(ABC):
    def __init__(self, next_logger):
        self.next_logger = next_logger

    @abstractmethod
    def log(self, log_level, message):
        if self.next_logger:
            self.next_logger.log(log_level, message)
        else:
            print("No log level")


class DebugLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level, message):
        if log_level == LogLevel.DEBUG:
            print("Debugger log", message)
        else:
            super().log(log_level, message)


class InfoLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level, message):
        if log_level == LogLevel.INFO:
            print("info log", message)
        else:
            super().log(log_level, message)


class WarningLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level, message):
        if log_level == LogLevel.WARNING:
            print("Warning log", message)
        else:
            super().log(log_level, message)


class ErrorLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level, message):
        if log_level == LogLevel.ERROR:
            print("Error log", message)
        else:
            super().log(log_level, message)


def get_logger_obj():
    debug_log = DebugLogger(InfoLogger(WarningLogger(ErrorLogger(None))))
    return debug_log


if __name__ == "__main__":
    logger = get_logger_obj()
    logger.log(LogLevel.DEBUG, "message 1")
    logger.log(LogLevel.ERROR, "message 2")
    logger.log(LogLevel.WARNING, "message 3")
    logger.log(LogLevel.INFO, "message 4")
    logger.log("", "message 2")

