
import socket
from typing import Dict

from pymt5.request import MT5Request
from pymt5.auth import MT5Auth
from pymt5.test import MT5Test
from pymt5.common import MT5Common
from pymt5.time import MT5Time
from pymt5.users import MT5Users
from pymt5.group import MT5Group
from pymt5.symbols import MT5Symbols
from pymt5.ticks import MT5Ticks

from pymt5.exceptions import MT5ConnectionError, MT5SocketError, MT5ResponseError
from pymt5.logger import MT5Logger
from pymt5.protocol import MT5BodyProtocol, MT5HeaderProtocol


class MT5Connect(object):

    HEADER_LENGTH = 9
    MAX_CLIENT_COMMAND = 16383

    port: int = None
    host: str = None
    timeout: int = None
    is_crypt: bool = None

    crypt = None

    number_command: int = 0

    log_level: str = ''

    __socket: socket = None

    def __init__(self, host: str, port: int, timeout: int = 5, is_crypt: bool = False, log_level: str = 'ERROR',
                 logger=None):
        """
        Connection init
        :param host: MT5 server host
        :type host: str
        :param port: MT5 server port
        :type port: int
        :param timeout: Connection timeout
        :type timeout: int
        :param is_crypt:
        :type is_crypt: bool
        :param log_level:
        :type log_level: str
        :param logger:
        """

        if not logger:
            self.logger = MT5Logger(self.__class__.__name__, level=log_level)
        else:
            self.logger = logger

        self.host = host
        self.port = port
        self.timeout = timeout
        self.is_crypt = is_crypt
        self.log_level = log_level

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self) -> bool:
        """
        Connect to MT5 server
        :return: Connect status
        """

        try:
            self.__socket = socket.create_connection(address=(self.host, self.port))
        except socket.error as e:
            raise MT5ConnectionError("Can't not connect to MT5 server: %s" % str(e))
        else:
            self.logger.debug("Successful connection")

        self.__socket.setblocking(True)

        """
        Set WebAPI Mode
        """
        try:
            self.__socket.send(b'MT5WEBAPI')
        except socket.error as e:
            raise MT5SocketError("Can't not set WebAPI mode: %s" % str(e))

        return True

    def send(self, command: str, options: Dict[str, str], data: str = None):
        """
        Send command to MT5 server
        :param command:
        :type command: str
        :param options:
        :type options: dict(str, str)
        :param data:
        :type data:
        :return:
        :rtype: bool
        """

        if not isinstance(self.__socket, socket.socket):
            message = "Connection is broken. Data can't be sent"
            self.logger.error(message)
            raise MT5SocketError(message)

        self.number_command = \
            (self.number_command + 1) if self.number_command < self.MAX_CLIENT_COMMAND else 0

        body = MT5BodyProtocol(
            command=command,
            options=options,
            data=data
        )

        body_data = self.crypt.crypt_packet(body.bytes) \
            if self.is_crypt and self.crypt else body.bytes

        header_data = MT5HeaderProtocol(
            body_size=len(body_data),
            number_command=self.number_command
        ).bytes

        request = str(body).replace('\r\n', ' ')
        self.logger.debug("Send data: " + request)

        try:
            self.__socket.send(header_data)
            self.__socket.sendall(body_data)
        except socket.error as e:
            raise MT5SocketError("Data can't be sent: %s" % str(e))

        return True

    def read(self) -> MT5BodyProtocol:
        """
        Read data from MT5 server
        :return:
        :rtype: MT5BodyProtocol
        :raises: MT5SocketError, MT5ResponseError
        """

        if not isinstance(self.__socket, socket.socket):
            raise MT5SocketError("Connection is broken. Data can't be read")

        body = None
        buffer = b''

        while True:

            try:
                header = self.__read_header()
            except socket.error as e:
                raise MT5SocketError("Data can't be read: %s" % str(e))

            if not header:
                raise MT5ResponseError("Data is empty")

            if not isinstance(header, MT5HeaderProtocol):
                raise MT5ResponseError("Incorrect header")

            try:

                if header.flag == 1:
                    buffer += self.__read_body_raw(header.body_size)
                else:
                    body = self.__read_body(header.body_size, buffer)

            except socket.error as e:
                raise MT5SocketError("Data can't be read: %s" % str(e))

            if header.number_command != self.number_command:

                if header.body_size != 0:
                    self.logger.debug(
                        "Number of packet incorrect. Need: %d, but get %d" %
                        (self.number_command, header.number_command, ))
                else:
                    self.logger.debug("PING Packet")

                continue

            if header.flag == 1:
                continue
            else:
                break

        if not isinstance(body, MT5BodyProtocol):
            raise MT5ResponseError("Incorrect body")

        response = str(body).replace('\r\n', ' ')
        self.logger.debug("Read data: " + response)

        return body

    def __read_header(self) -> MT5HeaderProtocol or bytes:
        """
        Read header package
        :return:
        :rtype: MT5HeaderProtocol or bytes
        """
        data = self.__socket.recv(MT5HeaderProtocol.HEADER_LENGTH)
        return MT5HeaderProtocol.parse(data) or data

    def __read_body(self, size: int, append: bytes = b'') -> MT5BodyProtocol or None:
        """
        Read body packages
        :param size:
        :return:
        :rtype: MT5BodyProtocol or None
        """

        buffer = b''

        while len(buffer) < size:
            packet = self.__socket.recv(size - len(buffer))

            if not packet:
                return None

            buffer += packet

        return MT5BodyProtocol.parse(append + self.crypt.decrypt_packet(buffer)) \
            if self.is_crypt and self.crypt else MT5BodyProtocol.parse(append + buffer)

    def __read_body_raw(self, size: int) -> bytes or None:
        """
        Read body raw
        :return:
        :rtype: bytes or None
        """

        buffer = b''

        while len(buffer) < size:
            packet = self.__socket.recv(size - len(buffer))

            if not packet:
                return None

            buffer += packet

        return self.crypt.decrypt_packet(buffer) if self.is_crypt else buffer

    def disconnect(self):
        """
        Disconnect
        :return:
        """

        try:
            self.__socket.send(b'QUIT')
            self.__socket.close()
        except Exception:
            pass

        self.logger.debug("Connection closed")

    def auth(self, login: int, password: str) -> bool:
        """
        Auth
        :param login:
        :param password:
        :return:
        """
        return MT5Auth(self, self.logger).auth(login, password)

    @property
    def request(self) -> MT5Request:
        """
        Base request
        :return:
        :rtype: MT5Request
        """
        return MT5Request(self)

    @property
    def test(self) -> MT5Test:
        """
        Test
        :return:
        :rtype: MT5Test
        """
        return MT5Test(self)

    @property
    def common(self) -> MT5Common:
        """
        Common
        :return:
        :rtype: MT5Common
        """
        return MT5Common(self)

    @property
    def time(self) -> MT5Time:
        """
        Time
        :return:
        :rtype: MT5Time
        """
        return MT5Time(self)

    @property
    def users(self) -> MT5Users:
        """
        Users
        :return:
        :rtype: MT5Users
        """
        return MT5Users(self)

    @property
    def group(self) -> MT5Group:
        """
        Group
        :return:
        :rtype: MT5Group
        """
        return MT5Group(self)

    @property
    def symbols(self) -> MT5Symbols:
        """
        Symbols
        :return:
        :rtype: MT5Symbols
        """
        return MT5Symbols(self)

    @property
    def ticks(self) -> MT5Ticks:
        """
        Ticks
        :return:
        :rtype: MT5Ticks
        """
        return MT5Ticks(self)
