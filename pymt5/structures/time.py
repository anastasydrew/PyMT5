from pymt5.structures.base import MT5BaseData


class MT5TimeData(MT5BaseData):

    daylight: int = None
    daylight_state: int = None
    time_zone: int = None
    time_server: str = None
    days: list = None
