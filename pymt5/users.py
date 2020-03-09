import json
from json import JSONDecodeError

from pymt5.exceptions import MT5Error
from pymt5.request import MT5Request
from pymt5.structures.user import MT5UserData


class MT5Users(MT5Request):

    @staticmethod
    def new() -> MT5UserData:
        return MT5UserData()

    def get(self, login: int) -> MT5UserData:
        """
        Get user information
        :param login:
        :type login: int
        :return:
        """
        response = self.send('USER_GET', {
            'LOGIN': str(login)
        })

        return MT5UserData.from_json(response.data)

    def add(self, user: MT5UserData) -> MT5UserData:
        """
        Add new user
        :param user:
        :type user: MT5UserData
        :return:
        """
        response = self.send('USER_ADD', {
            'LOGIN': str(user.login),
            'GROUP': user.group,
            'RIGHTS': user.rights,
            'PASS_MAIN': user.pass_main,
            'PASS_INVESTOR': user.pass_investor,
            'NAME': user.name,
            'COMPANY': user.company,
            'LANGUAGE': user.language,
            'CITY': user.city,
            'STATE': user.state,
            'ZIPCODE': user.zip_code,
            'ADDRESS': user.address,
            'PHONE': user.phone,
            'EMAIL': user.email,
            'ID': user.id,
            'STATUS': user.status,
            'COMMENT': user.comment,
            'COLOR': user.color,
            'PASS_PHONE': user.color,
            'LEVERAGE': user.leverage,
            'AGENT': user.agent,
        }, data=user.to_json())

        return MT5UserData.from_json(response.data)

    def delete(self, login: int):
        """
        Delete user
        :param login:
        :return:
        """
        self.send('USER_DELETE', {
            'LOGIN': str(login)
        })

    def update(self, user: MT5UserData) -> MT5UserData:
        """
        Update user
        :param user:
        :type user: MT5UserData
        :return:
        """
        return self.add(user)

    def list(self, group: str) -> list:
        """
        Get user logins
        :param group:
        :type group: str
        :rtype: list
        :return:
        """

        response = self.send('USER_LOGINS', {
            'GROUP': group
        })

        try:
            data = json.loads(response.data)
        except JSONDecodeError:
            raise MT5Error("Can't parse data")

        if not isinstance(data, list):
            raise MT5Error("Data is not list")

        return data
