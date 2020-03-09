import sys
import logging
from logging import StreamHandler


class MT5Logger(object):

    levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR
    }

    name = None
    logger = None
    loggers = {}

    def __init__(self, name='', level='DEBUG'):
        """
        Init logger class
        :param name: Logger name
        :type name: str
        """

        self.name = name

        if name in self.__class__.loggers:
            self.logger = self.__class__.loggers[name]
        else:
            self.logger = logging.getLogger(name)
            self.logger.addHandler(self.get_handler())
            self.__class__.loggers[name] = self.logger

        self.logger.setLevel(self.levels[level])

    @staticmethod
    def get_handler():
        """
        Get stream handler
        :return:
        :rtype: StreamHandler
        """
        stream_handler = StreamHandler(stream=sys.stderr)
        formatter = logging.Formatter('%(asctime)s [%(name)s/%(levelname)s]: %(message)s')
        stream_handler.setFormatter(formatter)

        return stream_handler

    def debug(self, message):
        """
        Debug message
        :param message:
        :type message: str
        :return:
        """
        self.logger.debug(message)

    def info(self, message):
        """
        Info message
        :param message:
        :type message: str
        :return:
        """
        self.logger.info(message)

    def warning(self, message):
        """
        Warning message
        :param message:
        :type message: str
        :return:
        """
        self.logger.warning(message)

    def error(self, message):
        """
        Error message
        :param message:
        :type message: str
        :return:
        """
        self.logger.error(message)
