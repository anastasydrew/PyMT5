from typing import Dict

from pymt5.exceptions import MT5RequestError, MT5ResponseError
from pymt5.protocol import MT5ReturnCodes
from pymt5.response import MT5Response


class MT5Request(object):

    __connect = None

    def __init__(self, connect):
        """
        :param connect:
        :type connect: MT5Connect
        """
        self.__connect = connect

    def send(self, command: str, params: Dict[str, str], data: str = None) -> MT5Response:
        """
        Send request and validate data
        :param command:
        :type command: str
        :param params:
        :type params: dict[str, str]
        :param data:
        :type data: str
        :return:
        :rtype: MT5Response
        :raise: MT5RequestError MT5ResponseError
        """

        if not self.__connect.send(command, params, data):
            raise MT5RequestError("Send request failed")

        body = self.__connect.read()

        if MT5ReturnCodes.PARAM not in body.options:
            raise MT5ResponseError("Can't read request status")

        if body.options[MT5ReturnCodes.PARAM] != MT5ReturnCodes.STATUS_DONE:
            raise MT5ResponseError("Request failed: " + body.options[MT5ReturnCodes.PARAM])

        return MT5Response(self.__connect, body)
