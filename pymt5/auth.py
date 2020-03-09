from hashlib import md5

from pymt5.crypt import MT5Crypt
from pymt5.protocol import VERSION
from pymt5.request import MT5Request
from pymt5.utils import MT5Utils


class MT5Auth(MT5Request):

    VAL_CRYPT_NONE = "NONE"
    VAL_CRYPT_AES256OFB = "AES256OFB"

    agent: str = None

    __connect = None

    def __init__(self, connect, logger, agent: str = 'PYMT5'):
        """
        Init
        :param connect:
        :type connect: MT5Connect
        :param agent:
        :type agent: str
        """
        super(MT5Auth, self).__init__(connect)
        self.logger = logger
        self.__connect = connect
        self.agent = agent

    def auth(self, login: int, password: str) -> bool:
        """
        Auth to MT5 server
        :param login:
        :type login: int
        :param password:
        :type password: str
        :return:
        :rtype: bool
        """

        """
        Auth start
        """
        response = self.send('AUTH_START', {
                'VERSION': VERSION,
                'AGENT': self.agent,
                'LOGIN': login,
                'TYPE': 'MANAGER',
                'CRYPT_METHOD': self.VAL_CRYPT_AES256OFB if self.__connect.is_crypt else self.VAL_CRYPT_NONE
            })

        """
        Auth answer
        """
        cli_rand = MT5Utils.get_random_hex(16)

        pass_hash = MT5Utils.get_hash_from_password(password)

        srv_rand_answ = md5(
            bytes.fromhex(pass_hash) +
            bytes.fromhex(response.get('SRV_RAND'))).hexdigest()

        response = self.send('AUTH_ANSWER', {
                'SRV_RAND_ANSWER': srv_rand_answ,
                'CLI_RAND': cli_rand
            })

        """
        Check auth user answer
        """

        cli_rand_answ = md5(
            bytes.fromhex(pass_hash) +
            bytes.fromhex(cli_rand)).hexdigest()

        if response.get('CLI_RAND_ANSWER') != cli_rand_answ:
            self.logger.error("Server return broken password hash")
            return False

        try:
            self.__connect.crypt = MT5Crypt(response.get('CRYPT_RAND'), pass_hash)
        except ValueError:
            self.logger.info("Cryptography disabled")

        return True


