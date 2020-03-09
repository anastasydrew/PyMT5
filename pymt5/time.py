from datetime import datetime

from pymt5.request import MT5Request
from pymt5.structures.time import MT5TimeData


class MT5Time(MT5Request):

    def get(self) -> MT5TimeData:
        """
        Get time configuration
        :return:
        """

        response = self.send('TIME_GET', {})
        return MT5TimeData.from_json(response.data)

    def server(self) -> datetime or None:
        """
        Get server time
        :return:
        :rtype: datetime or None
        """

        response = self.send('TIME_SERVER', {})

        try:
            return datetime.utcfromtimestamp(int(response.get('TIME').split(' ')[0]))
        except (IndexError, ValueError, TypeError):
            return None

