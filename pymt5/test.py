from pymt5.exceptions import MT5Error
from pymt5.request import MT5Request


class MT5Test(MT5Request):

    def trade(self) -> bool:
        """
        Test trade
        :return:
        :rtype: bool
        """

        try:
            self.send('TEST_TRADE', {})
        except MT5Error:
            return False

        return True

    def access(self) -> bool:
        """
        Test access
        :return:
        :rtype: bool
        """

        try:
            self.send('TEST_ACCESS', {})
        except MT5Error:
            return False

        return True
