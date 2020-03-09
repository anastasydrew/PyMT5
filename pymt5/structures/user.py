from pymt5.structures.base import MT5BaseData


class MT5UserData(MT5BaseData):

    fields = {'login': 'Login', 'group': 'Group', 'cert_serial_number': 'CertSerialNumber', 'rights': 'Rights',
              'mqid': 'MQID', 'registration': 'Registration', 'last_access': 'LastAccess',
              'last_pass_change': 'LastPassChange', 'last_ip': 'LastIP', 'name': 'Name', 'company': 'Company',
              'account': 'Account', 'country': 'Country', 'language': 'Language', 'client_id': 'ClientID',
              'city': 'City', 'state': 'State', 'zip_code': 'ZipCode', 'address': 'Address', 'phone': 'Phone',
              'email': 'Email', 'id': 'ID', 'status': 'Status', 'comment': 'Comment', 'color': 'Color',
              'phone_password': 'PhonePassword', 'leverage': 'Leverage', 'agent': 'Agent',
              'currency_digits': 'CurrencyDigits', 'balance': 'Balance', 'credit': 'Credit',
              'interest_rate': 'InterestRate', 'commission_daily': 'CommissionDaily',
              'commission_monthly': 'CommissionMonthly', 'commission_agent_daily': 'CommissionAgentDaily',
              'commission_agent_monthly': 'CommissionAgentMonthly', 'balance_prev_day': 'BalancePrevDay',
              'balance_prev_month': 'BalancePrevMonth', 'equity_prev_day': 'EquityPrevDay',
              'equity_prev_month': 'EquityPrevMonth', 'trade_accounts': 'TradeAccounts',
              'lead_campaign': 'LeadCampaign', 'lead_source': 'LeadSource'}

    class UserRights(object):
        none = 0x0000000000000000
        enabled = 0x0000000000000001
        password = 0x0000000000000002
        trade_disabled = 0x0000000000000004
        investor = 0x0000000000000008
        confirmed = 0x0000000000000010
        trailing = 0x0000000000000020
        expert = 0x0000000000000040
        api = 0x0000000000000080
        reports = 0x0000000000000100
        readonly = 0x0000000000000200
        reset_pass = 0x0000000000000400
        otp_enabled = 0x0000000000000800
        
    login: int = None
    group: str = None
    pass_main: str = None
    pass_investor: str = None
    cert_serial_number: int = None
    rights: int = None  # UserRights
    mqid: str = None
    registration: int = None
    last_access: int = None
    last_pass_change: int = None
    last_ip: str = None
    name: str = None
    company: str = None
    account: str = None
    country: str = None
    language: int = None
    client_id: str = None
    city: str = None
    state: str = None
    zip_code: str = None
    address: str = None
    phone: str = None
    email: str = None
    id: str = None
    status: str = None
    comment: str = None
    color: int = None
    phone_password: str = None
    leverage: int = None
    agent: int = None
    currency_digits: int = None
    balance: float = None
    credit: float = None
    interest_rate: float = None
    commission_daily: float = None
    commission_monthly: float = None
    commission_agent_daily: float = None
    commission_agent_monthly: float = None
    balance_prev_day: float = None
    balance_prev_month: float = None
    equity_prev_day: float = None
    equity_prev_month: float = None
    trade_accounts: list = None
    lead_campaign: str = None
    lead_source: str = None

    def __str__(self):
        return str(self.login)