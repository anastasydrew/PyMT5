from typing import List

from pymt5.request import MT5Request
from pymt5.structures.group import MT5GroupData


class MT5Group(MT5Request):

    @staticmethod
    def new() -> MT5GroupData:
        return MT5GroupData()

    def get(self, group: str) -> MT5GroupData:
        """
        Get group
        :param group:
        :type group: str
        :return:
        """
        response = self.send('GROUP_GET', {
            'GROUP': group
        })

        return MT5GroupData.from_json(response.data)

    def add(self, group: MT5GroupData) -> MT5GroupData:
        """
        Add group
        :param group:
        :type group: MT5GroupData
        :return:
        """
        response = self.send('GROUP_ADD', {}, data=group.to_json())
        return MT5GroupData.from_json(response.data)

    def delete(self, group: str):
        """
        Delete group
        :param group:
        :type group: str
        :return:
        """
        self.send('GROUP_DELETE', {
            'GROUP': group
        })

    def total(self) -> int:
        """
        Get total group
        :return:
        """
        response = self.send('GROUP_TOTAL', {})
        return response.get_int('TOTAL')

    def next(self, index: int) -> MT5GroupData:
        """
        Get group from index
        :param index:
        :return:
        """
        response = self.send('GROUP_NEXT', {
            'INDEX': str(index),
        })

        return MT5GroupData.from_json(response.data)

    def all(self) -> List[MT5GroupData]:
        """
        Get all groups
        :return:
        """

        result = []

        total = self.total()

        for idx in range(total):
            result.append(self.next(idx))

        return result

