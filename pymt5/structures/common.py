# from datetime import datetime

from pymt5.structures.base import MT5BaseData


class MT5CommonData(MT5BaseData):
    """
    MT5CommonData
    """

    name: str = None
    owner: str = None
    owner_email: str = None
    owner_host: str = None
    owner_id: str = None
    product: str = None

    account_auto: int = None
    account_url: str = None
    expiration_license: int = None
    expiration_support: int = None

    limit_accounts: int = None
    limit_deals: int = None
    limit_groups: int = None
    limit_symbols: int = None
    limit_trade_servers: int = None
    limit_web_servers: int = None
    live_update_mode: int = None

    total_deals: int = None
    total_orders: int = None
    total_orders_history: int = None
    total_positions: int = None
    total_users: int = None
    total_users_real: int = None

    def __str__(self):
        return '{} - {}'.format(self.owner, self.name)
