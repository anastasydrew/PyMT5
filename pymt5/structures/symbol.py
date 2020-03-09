from pymt5.structures.base import MT5BaseData


class MT5SymbolData(MT5BaseData):

    fields = {'accrued_interest': 'AccruedInterest', 'basis': 'Basis', 'calc_mode': 'CalcMode', 'color': 'Color',
              'color_background': 'ColorBackground', 'contract_size': 'ContractSize', 'currency_base': 'CurrencyBase',
              'currency_base_digits': 'CurrencyBaseDigits', 'currency_margin': 'CurrencyMargin',
              'currency_margin_digits': 'CurrencyMarginDigits', 'currency_profit': 'CurrencyProfit',
              'currency_profit_digits': 'CurrencyProfitDigits', 'description': 'Description', 'digits': 'Digits',
              'exec_mode': 'ExecMode', 'expir_flags': 'ExpirFlags', 'face_value': 'FaceValue',
              'fill_flags': 'FillFlags',
              'filter_discard': 'FilterDiscard', 'filter_gap': 'FilterGap', 'filter_gap_ticks': 'FilterGapTicks',
              'filter_hard': 'FilterHard', 'filter_hard_ticks': 'FilterHardTicks', 'filter_soft': 'FilterSoft',
              'filter_soft_ticks': 'FilterSoftTicks', 'filter_spread_max': 'FilterSpreadMax',
              'filter_spread_min': 'FilterSpreadMin', 'freeze_level': 'FreezeLevel', 'gtc_mode': 'GTCMode',
              'ie_check_mode': 'IECheckMode', 'ie_slip_losing': 'IESlipLosing', 'ie_slip_profit': 'IESlipProfit',
              'ie_timeout': 'IETimeout', 'ie_volume_max': 'IEVolumeMax', 'ie_volume_max_ext': 'IEVolumeMaxExt',
              'international': 'International', 'isin': 'ISIN', 'margin_currency': 'MarginCurrency',
              'margin_flags': 'MarginFlags', 'margin_hedged': 'MarginHedged', 'margin_initial': 'MarginInitial',
              'margin_initial_buy': 'MarginInitialBuy', 'margin_initial_buy_limit': 'MarginInitialBuyLimit',
              'margin_initial_buy_stop': 'MarginInitialBuyStop',
              'margin_initial_buy_stop_limit': 'MarginInitialBuyStopLimit',
              'margin_initial_sell': 'MarginInitialSell', 'margin_initial_sell_limit': 'MarginInitialSellLimit',
              'margin_initial_sell_stop': 'MarginInitialSellStop',
              'margin_initial_sell_stop_limit': 'MarginInitialSellStopLimit', 'margin_liquidity': 'MarginLiquidity',
              'margin_maintenance': 'MarginMaintenance', 'margin_maintenance_buy': 'MarginMaintenanceBuy',
              'margin_maintenance_buy_limit': 'MarginMaintenanceBuyLimit',
              'margin_maintenance_buy_stop': 'MarginMaintenanceBuyStop',
              'margin_maintenance_buy_stop_limit': 'MarginMaintenanceBuyStopLimit',
              'margin_maintenance_sell': 'MarginMaintenanceSell',
              'margin_maintenance_sell_limit': 'MarginMaintenanceSellLimit',
              'margin_maintenance_sell_stop': 'MarginMaintenanceSellStop',
              'margin_maintenance_sell_stop_limit': 'MarginMaintenanceSellStopLimit', 'multiply': 'Multiply',
              'option_mode': 'OptionMode', 'order_flags': 'OrderFlags', 'page': 'Page', 'path': 'Path',
              'point': 'Point',
              'price_limit_max': 'PriceLimitMax', 'price_limit_min': 'PriceLimitMin', 'price_settle': 'PriceSettle',
              'price_strike': 'PriceStrike', 'quotes_timeout': 'QuotesTimeout', 're_flags': 'REFlags',
              're_timeout': 'RETimeout', 'sessions_quotes': 'SessionsQuotes', 'sessions_trades': 'SessionsTrades',
              'source': 'Source', 'splice_time_days': 'SpliceTimeDays', 'splice_time_type': 'SpliceTimeType',
              'splice_type': 'SpliceType', 'spread': 'Spread', 'spread_balance': 'SpreadBalance',
              'spread_diff': 'SpreadDiff',
              'spread_diff_balance': 'SpreadDiffBalance', 'stops_level': 'StopsLevel', 'swap_long': 'SwapLong',
              'swap_mode': 'SwapMode', 'swap_short': 'SwapShort', 'symbol': 'Symbol',
              'tick_book_depth': 'TickBookDepth',
              'tick_chart_mode': 'TickChartMode', 'tick_flags': 'TickFlags', 'tick_size': 'TickSize',
              'tick_value': 'TickValue', 'time_expiration': 'TimeExpiration', 'time_start': 'TimeStart',
              'trade_flags': 'TradeFlags', 'trade_mode': 'TradeMode', 'volume_limit': 'VolumeLimit',
              'volume_limit_ext': 'VolumeLimitExt', 'volume_max': 'VolumeMax', 'volume_max_ext': 'VolumeMaxExt',
              'volume_min': 'VolumeMin', 'volume_min_ext': 'VolumeMinExt', 'volume_step': 'VolumeStep',
              'volume_step_ext': 'VolumeStepExt'}

    class TickFlags(object):
        none = 0
        realtime = 1
        collectraw = 2
        feed_stats = 3
        all = 7

    class TradeMode(object):
        disabled = 0
        long_only = 1
        short_only = 2
        close_only = 3
        full = 4

    class CalcMode(object):
        forex = 0
        futures = 1
        cfd = 2
        cfd_index = 3
        cfd_leverage = 4
        forex_no_leverage = 5
        exch_stocks = 32
        exch_futures = 33
        exch_forts = 34
        exch_options = 35
        exch_options_margin = 36
        exch_bonds = 37
        exch_stoocks_moex = 38
        exch_bonds_moex = 39
        serv_colleteral = 64

    class ExecutionMode(object):
        request = 0
        instant = 1
        market = 2
        exchange = 3

    class GTCMode(object):
        gtc = 0
        daily = 1
        daily_no_stops = 2

    class FillingFlags(object):
        none = 0
        fok = 1
        ioc = 2
        all = 3

    class ExpirationFlags(object):
        none = 0
        gtc = 1
        day = 2
        specified = 4
        specified_day = 8
        all = 15

    class MarginFlags(object):
        none = 0
        check_process = 1
        check_sltp = 2
        hedge_large_leg = 4

    class SwapMode(object):
        disabled = 0
        by_points = 1
        by_symbol_currency = 2
        by_margin_currency = 3
        by_group_currency = 4
        by_interest_current = 5
        by_interest_open = 6
        reopen_by_close_price = 7
        reopen_by_bid = 8
        by_profit_currency = 9

    class RequestFlags(object):
        none = 0
        order = 1

    class TradeFlags(object):
        none = 0
        profit_by_market = 1
        allow_signals = 2
        all = 3

    class OrderFlags(object):
        none = 0
        market = 1
        limit = 2
        stop = 4
        stop_limit = 8
        sl = 16
        tp = 32
        close_by = 64
        all = 127

    class ChartMode(object):
        bid_price = 0
        last_price = 1
        old = 255

    class OptionMode(object):
        european_call = 0
        european_put = 1
        american_call = 2
        american_put = 3

    symbol: str = None
    path: str = None
    isin: str = None
    description: str = None
    international: str = None
    basis: str = None
    source: str = None
    page: str = None
    currency_base: str = None
    currency_base_digits: int = None
    currency_margin: str = None
    currency_margin_digits: int = None
    currency_profit: str = None
    currency_profit_digits: int = None
    color: int = None
    color_background: int = None
    digits: int = None
    point: float = None
    multiply: float = None
    tick_flags: int = None  # TickFlags
    tick_book_depth: int = None
    tick_chart_mode: int = None
    filter_discard: int = None
    filter_gap: int = None
    filter_gap_ticks: int = None
    filter_hard: int = None
    filter_hard_ticks: int = None
    filter_soft: int = None
    filter_soft_ticks: int = None
    filter_spread_max: int = None
    filter_spread_min: int = None
    trade_mode: int = None  # TradeMode
    trade_flags: int = None  # TradeFlags
    calc_mode: int = None  # CalcMode
    exec_mode: int = None  # ExecutionMode
    gtc_mode: int = None  # GTCMode
    fill_flags = None  # FillingFlags
    expir_flags: int = None  # ExpirationFlags
    order_flags: int = None  # OrderFlags
    spread: int = None
    spread_balance: int = None
    spread_diff: int = None
    spread_diff_balance: int = None
    tick_value: float = None
    tick_size: float = None
    contract_size: float = None
    stops_level: int = None
    freeze_level: int = None
    quotes_timeout: int = None
    volume_limit: int = None
    volume_limit_ext: int = None
    volume_max: int = None
    volume_max_ext: int = None
    volume_min: int = None
    volume_min_ext: int = None
    volume_step: int = None
    volume_step_ext: int = None
    margin_flags: int = None  # MarginFlags
    margin_initial: float = None
    margin_maintenance: float = None
    margin_initial_buy: float = None
    margin_initial_buy_limit: float = None
    margin_initial_buy_stop: float = None
    margin_initial_buy_stop_limit: float = None
    margin_initial_sell: float = None
    margin_initial_sell_limit: float = None
    margin_initial_sell_stop: float = None
    margin_initial_sell_stop_limit: float = None
    margin_maintenance_buy: float = None
    margin_maintenance_buy_limit: float = None
    margin_maintenance_buy_stop: float = None
    margin_maintenance_buy_stop_limit: float = None
    margin_maintenance_sell: float = None
    margin_maintenance_sell_limit: float = None
    margin_maintenance_sell_stop: float = None
    margin_maintenance_sell_stop_limit: float = None
    margin_liquidity: float = None
    margin_hedged: float = None
    margin_currency = None
    swap_mode: int = None  # SwapMode
    swap_long: float = None
    swap_short: float = None
    swap3_day: float = None
    time_start: int = None
    time_expiration: int = None
    sessions_quotes: list = None
    sessions_trades: list = None
    re_flags: int = None  # RequestFlags
    re_timeout: int = None
    ie_check_mode: int = None
    ie_slip_losing: int = None
    ie_slip_profit: int = None
    ie_timeout: int = None
    ie_volume_max: int = None
    ie_volume_max_ext: int = None
    price_settle: float = None
    price_limit_max: float = None
    price_limit_min: float = None
    price_strike: float = None
    option_mode: int = None  # OptionMode
    face_value = None
    accrued_interest: float = None
    splice_time_days: int = None
    splice_time_type: int = None
    splice_type: int = None

    def __str__(self):
        return self.symbol
