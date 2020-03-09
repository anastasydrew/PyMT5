from typing import List

from pymt5.request import MT5Request
from pymt5.structures.tick import MT5TickShortData, MT5TickData


class MT5Ticks(MT5Request):

    tick_last_trans_id = 0
    tick_stat_trans_id = 0

    def last(self, symbol: str) -> List[MT5TickShortData]:
        """
        Get tick last
        :param symbol:
        :type symbol: str
        :rtype: list[MT5TickShortData]
        :return:
        """

        response = self.send('TICK_LAST', {
            'SYMBOL': symbol,
            'TRANS_ID': self.tick_last_trans_id
        })

        self.tick_last_trans_id = response.get('TRANS_ID')
        return MT5TickShortData.from_list_json(response.data)

    def stat(self, symbol: str) -> List[MT5TickData]:
        """
        Get tick last stat
        :param symbol:
        :type symbol: str
        :rtype: list[MT5TickData]
        :return:
        """

        response = self.send('TICK_STAT', {
            'SYMBOL': symbol,
            'TRANS_ID': self.tick_stat_trans_id
        })

        self.tick_stat_trans_id = response.get('TRANS_ID')
        return MT5TickData.from_list_json(response.data)
