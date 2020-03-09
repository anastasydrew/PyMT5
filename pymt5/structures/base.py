import json
import re
from json import JSONDecodeError
from typing import get_type_hints

from pymt5.exceptions import MT5Error


class MT5BaseData(object):

    fields = {}

    @classmethod
    def from_json(cls, data):
        """
        Make class from json
        :param data:
        :return:
        """

        try:
            data = json.loads(data)
        except JSONDecodeError:
            raise MT5Error("Can't parse parse data structure")

        if not isinstance(data, dict):
            raise MT5Error("Broken structure")

        return cls.__from_dict(data)

    @classmethod
    def from_list_json(cls, data) -> list:
        """
        Make list of data from json
        :param data:
        :return:
        """

        result = []

        try:
            data = json.loads(data)
        except JSONDecodeError:
            raise MT5Error("Can't parse data structure")

        if not isinstance(data, list):
            raise MT5Error("Broken structure")

        for item in data:

            if not isinstance(item, dict):
                raise MT5Error("Broken structure")

            result.append(cls.__from_dict(item))

        return result

    @classmethod
    def __from_dict(cls, data: dict):
        """
        Dict to data structure
        :param data:
        :return:
        """

        result = cls()
        result.fields = {}
        result.order = []

        types = get_type_hints(cls)

        for key in data.keys():
            attr = MT5BaseData.camel_to_snake(key)
            result.fields[attr] = key
            result.order.append(attr)

            try:
                if hasattr(result, 'set_' + attr) \
                        and callable(getattr(result, 'set_' + attr)):
                    getattr(result, 'set_' + attr)(data[key])

                elif attr in types and callable(types[attr]):
                    setattr(result, attr, types[attr](data[key]))

                else:
                    setattr(result, attr, data[key])

            except Exception as e:
                setattr(result, attr, data[key])

        return result

    def to_json(self):
        """
        Dump data class to json
        :return:
        """

        result = {}

        for key, val in self.fields.items():
            attr = getattr(self, key)
            if attr is not None:
                result[val] = attr

        return json.dumps(result)

    @staticmethod
    def camel_to_snake(text) -> str:
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

