import json

from pymt5.structures.base import MT5BaseData


class MT5GroupData(MT5BaseData):

    fields = {'auth_mode': 'AuthMode', 'auth_otp_mode': 'AuthOTPMode', 'auth_password_min': 'AuthPasswordMin',
              'commissions': 'Commissions', 'company': 'Company', 'company_catalog': 'CompanyCatalog',
              'company_email': 'CompanyEmail', 'company_page': 'CompanyPage',
              'company_support_email': 'CompanySupportEmail',
              'company_support_page': 'CompanySupportPage', 'currency': 'Currency', 'currency_digits': 'CurrencyDigits',
              'demo_deposit': 'DemoDeposit', 'demo_leverage': 'DemoLeverage', 'group': 'Group',
              'limit_history': 'LimitHistory', 'limit_orders': 'LimitOrders', 'limit_positions': 'LimitPositions',
              'limit_symbols': 'LimitSymbols', 'mail_mode': 'MailMode', 'margin_call': 'MarginCall',
              'margin_flags': 'MarginFlags', 'margin_free_mode': 'MarginFreeMode',
              'margin_free_profit_mode': 'MarginFreeProfitMode', 'margin_mode': 'MarginMode',
              'margin_so_mode': 'MarginSOMode', 'margin_stop_out': 'MarginStopOut', 'news_category': 'NewsCategory',
              'news_langs': 'NewsLangs', 'news_mode': 'NewsMode', 'permissions_flags': 'PermissionsFlags',
              'reports_email': 'ReportsEmail', 'reports_flags': 'ReportsFlags', 'reports_mode': 'ReportsMode',
              'server': 'Server', 'symbols': 'Symbols', 'trade_flags': 'TradeFlags',
              'trade_interestrate': 'TradeInterestrate', 'trade_transfer_mode': 'TradeTransferMode',
              'trade_virtual_credit': 'TradeVirtualCredit'}

    class Permissions(object):
        none = 0x00000000
        cert_confirm = 0x00000001
        enable_connection = 0x00000002
        reset_password = 0x00000004
        forced_otp_usage = 0x00000008
        risk_warning = 0x00000010
        regulation_protect = 0x00000020

    class AuthMode(object):
        auth_standard = 0
        auth_rsa1024 = 1
        auth_rsa2048 = 2
        auth_rsa_custom = 4

    class AuthOTPMode(object):
        disabled = 0
        otp_sha256 = 1
        otp_sha256_web = 2

    class ReportsMode(object):
        disabled = 0
        standard = 1

    class ReportsFlags(object):
        none = 0
        email = 1
        support = 2

    class NewsMode(object):
        disabled = 0
        headers = 1
        full = 2

    class MailMode(object):
        disabled = 0
        full = 1

    class TradeFlags(object):
        none = 0x00000000
        swaps = 0x00000001
        trailing = 0x00000002
        experts = 0x00000004
        expiration = 0x00000008
        signals_all = 0x00000010
        signals_own = 0x00000020
        so_compensation = 0x00000040
        so_fully_hedged = 0x00000080
        fifo_close = 0x00000100

    class TradeTransferMode(object):
        disabled = 0
        name = 1
        group = 2
        name_group = 3

    class MarginMode(object):
        retail = 0
        exchange_discount = 1
        retail_hedged = 2

    class MarginFlags(object):
        none = 0
        clear_acc = 1

    class MarginStopOutMode(object):
        percent = 0
        money = 1

    class MarginFreeMode(object):
        not_use_pl = 0
        use_pl = 1
        profit = 2
        loss = 3

    class MarginFreeProfitMode(object):
        profit_pl = 0
        profit_loss = 1

    class HistoryLimit(object):
        all = 0
        one_month = 1
        three_months = 2
        six_months = 3
        one_year = 4
        two_years = 5
        three_years = 6

    group: str = None
    server: int = None
    permissions_flags: int = None  # Permissions
    auth_mode: int = None  # AuthMode
    auth_password_min: int = None
    auth_otp_mode: int = None  # AuthOTPMode
    company: str = None
    company_page: str = None
    company_email: str = None
    company_support_page: str = None
    company_support_email: str = None
    company_catalog: str = None
    currency: str = None
    currency_digits: int = None
    reports_mode: int = None  # ReportsMode
    reports_flags: int = None  # ReportsFlags
    reports_email: str = None
    news_mode: int = None  # NewsMode
    news_category: str = None
    news_langs: str = None
    mail_mode: int = None  # MailMode
    trade_flags: int = None  # TradeFlags
    trade_transfer_mode: int = None  # TradeTransferMode
    trade_interestrate: float = None
    trade_virtual_credit: float = None
    margin_mode: int = None  # MarginMode
    margin_flags: int = None  # MarginFlags
    margin_so_mode: int = None  # MarginStopOutMode
    margin_free_mode: int = None  # MarginFreeMode
    margin_call: float = None
    margin_stop_out: float = None
    margin_free_profit_mode: int = None  # MarginFreeProfitMode
    demo_leverage: int = None
    demo_deposit: float = None
    limit_history: int = None  # HistoryLimit
    limit_orders: int = None
    limit_symbols: int = None
    limit_positions: int = None
    commissions: list = None
    symbols: list = None

    def __str__(self):
        return self.group
