from pymt5.request import MT5Request
from pymt5.structures.common import MT5CommonData


class MT5Common(MT5Request):

    def get(self) -> MT5CommonData:
        """
        Get common information
        :return:
        :rtype: MT5CommonData
        """

        response = self.send('COMMON_GET', {})
        return MT5CommonData.from_json(response.data)
