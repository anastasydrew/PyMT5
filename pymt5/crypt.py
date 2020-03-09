from hashlib import md5

from pymt5.aes256 import MT5Aes256


class MT5Crypt(object):

    aes_key = None
    iv_in = None
    iv_out = None

    aes_out = None
    aes_in = None
    crypt_out = None
    crypt_in = None

    def __init__(self, crypt_rand: str, pass_hash: str):
        """
        Init cryptographer
        :param crypt_rand:
        :type crypt_rand: str
        :param pass_hash:
        :type pass_hash: str
        """

        if len(crypt_rand) < 32 * 4 or len(crypt_rand) % 32 != 0:
            raise ValueError("Crypt rand is broken")

        if len(pass_hash) != 32:
            raise ValueError("Client rand is broken")

        keys = []

        for index in range(0, len(crypt_rand), 32):
            keys.append(md5(
                bytes.fromhex(crypt_rand[index:index + 32]) +
                bytes.fromhex(pass_hash if not keys else keys[-1])
            ).hexdigest())

        self.aes_key = bytes.fromhex(keys[0] + keys[1])
        self.iv_out = bytes.fromhex(keys[2])
        self.iv_in = bytes.fromhex(keys[3])

    def crypt_packet(self, packet: bytes) -> bytes:
        """
        Crypt sending data
        :param packet:
        :type packet: bytes
        :return:
        :rtype: bytes
        """

        result = b''

        if not self.crypt_out:
            self.crypt_out = MT5Aes256(self.aes_key)
            self.aes_out = self.iv_out

        for i in range(0, len(packet)):

            if i % 16 == 0:
                self.aes_out = self.crypt_out.encrypt_block(self.aes_out)

            result += bytes([packet[i] ^ self.aes_out[i % 16]])

        return result

    def decrypt_packet(self, packet: bytes) -> bytes:
        """
        Decrypt package
        :param packet:
        :type packet: bytes
        :return:
        :rtype: bytes
        """

        result = b''

        if not self.crypt_in:
            self.crypt_in = MT5Aes256(self.aes_key)
            self.aes_in = self.iv_in

        for i in range(0, len(packet)):

            if i % 16 == 0:
                self.aes_in = self.crypt_in.encrypt_block(self.aes_in)

            result += bytes([packet[i] ^ self.aes_in[i % 16]])

        return result
