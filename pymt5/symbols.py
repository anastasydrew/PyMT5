from typing import List

from pymt5.request import MT5Request
from pymt5.structures.symbol import MT5SymbolData


class MT5Symbols(MT5Request):

    @staticmethod
    def new(self) -> MT5SymbolData:
        return MT5SymbolData()

    def get(self, symbol: str) -> MT5SymbolData:
        """
        Get symbol by name
        :param symbol:
        :type symbol: str
        :rtype: MT5SymbolData
        :return:
        """
        response = self.send('SYMBOL_GET', {
            'SYMBOL': symbol
        })

        return MT5SymbolData.from_json(response.data)

    def group(self, symbol: str, group: str) -> MT5SymbolData:
        """
        Get symbol by name and group
        :param symbol:
        :type symbol: str
        :param group:
        :type group: str
        :rtype: MT5SymbolData
        :return:
        """
        response = self.send('SYMBOL_GET_GROUP', {
            'SYMBOL': symbol,
            'GROUP': group
        })

        return MT5SymbolData.from_json(response.data)

    def next(self, index: int = 0) -> MT5SymbolData:
        """
        Get symbol by index
        :param index:
        :type index: int
        :rtype: MT5SymbolData
        :return:
        """

        response = self.send('SYMBOL_NEXT', {
            'INDEX': str(index)
        })

        return MT5SymbolData.from_json(response.data)

    def add(self, data: MT5SymbolData) -> MT5SymbolData:
        """
        Set symbol data
        :param data:
        :type data: MT5SymbolData
        :rtype: MT5SymbolData
        :return:
        """

        response = self.send('SYMBOL_ADD', {}, data.to_json())
        return MT5SymbolData.from_json(response.data)

    def total(self) -> int:
        """
        Get total count symbols
        :return:
        :rtype: int
        """

        response = self.send('SYMBOL_TOTAL', {})
        return response.get_int('TOTAL')

    def all(self) -> List[MT5SymbolData]:
        """
        Get all symbols
        :rtype: list[MT5SymbolData]
        :return:
        """

        result = []

        total = self.total()

        for index in range(total):
            result.append(self.next(index))

        return result
