from pymt5.exceptions import MT5ResponseError


class MT5Response(object):

    __connect = None

    def __init__(self, connect, body):
        """
        :param connect:
        :type connect: MT5Connect
        :param body:
        :type body: MT5BodyProtocol
        """
        self.__connect = connect
        self.__body = body

    @property
    def data(self) -> str:
        """
        Get response body
        :return:
        :rtype: str
        :raise: MT5ResponseError
        """

        if not self.__body or self.__body.data is None:
            raise MT5ResponseError("Get data failed")

        return self.__body.data

    def get(self, param: str) -> str:
        """
        Get param
        :param param:
        :type param: str
        :return:
        :raise: MT5ResponseError
        """

        if param not in self.__body.options:
            raise MT5ResponseError("Param not found")

        return self.__body.options[param]

    def get_int(self, param: str) -> int:
        """
        Get int param
        :param param:
        :type param: str
        :return:
        :raise: MT5ResponseError
        """

        try:
            return int(self.get(param))
        except ValueError:
            raise MT5ResponseError("Param can't convert to int")

