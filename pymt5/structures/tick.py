from pymt5.structures.base import MT5BaseData


class MT5TickShortData(MT5BaseData):
    
    fields = {'symbol': 'Symbol', 'digits': 'Digits', 'datetime': 'Datetime', 'datetime_msc': 'DatetimeMsc',
              'bid': 'Bid', 'ask': 'Ask', 'last': 'Last', 'volume': 'Volume', 'volume_real': 'VolumeReal'}

    symbol: str = None
    digits: int = None
    datetime: int = None
    datetime_msc: int = None
    bid: float = None
    ask: float = None
    last: float = None
    volume: int = None
    volume_real: float = None

    def __str__(self):
        return self.symbol


class MT5TickData(MT5BaseData):

    fields = {'symbol': 'Symbol', 'digits': 'Digits', 'datetime': 'Datetime', 'datetime_msc': 'DatetimeMsc',
              'bid': 'Bid', 'bid_low': 'BidLow', 'bid_high': 'BidHigh', 'bid_dir': 'BidDir', 'ask': 'Ask',
              'ask_low': 'AskLow', 'ask_high': 'AskHigh', 'ask_dir': 'AskDir', 'last': 'Last', 'last_low': 'LastLow',
              'last_high': 'LastHigh', 'last_dir': 'LastDir', 'volume': 'Volume', 'volume_real': 'VolumeReal',
              'volume_low': 'VolumeLow', 'volume_low_real': 'VolumeLowReal', 'volume_high': 'VolumeHigh',
              'volume_high_real': 'VolumeHighReal', 'volume_dir': 'VolumeDir', 'trade_deals': 'TradeDeals',
              'trade_volume': 'TradeVolume', 'trade_volume_real': 'TradeVolumeReal', 'trade_turnover': 'TradeTurnover',
              'trade_interest': 'TradeInterest', 'trade_buy_orders': 'TradeBuyOrders',
              'trade_buy_volume': 'TradeBuyVolume', 'trade_buy_volume_real': 'TradeBuyVolumeReal',
              'trade_sell_orders': 'TradeSellOrders', 'trade_sell_volume': 'TradeSellVolume',
              'trade_sell_volume_real': 'TradeSellVolumeReal', 'price_open': 'PriceOpen', 'price_close': 'PriceClose',
              'price_change': 'PriceChange', 'price_volatility': 'PriceVolatility',
              'price_theoretical': 'PriceTheoretical'}

    symbol: str = None
    digits: int = None
    datetime: int = None
    datetime_msc: int = None
    bid: float = None
    bid_low: float = None
    bid_high: float = None
    bid_dir: int = None
    ask: float = None
    ask_low: float = None
    ask_high: float = None
    ask_dir: int = None
    last: float = None
    last_low: float = None
    last_high: float = None
    last_dir: int = None
    volume: int = None
    volume_real: int = None
    volume_low: int = None
    volume_low_real: int = None
    volume_high: int = None
    volume_high_real: int = None
    volume_dir: int = None
    trade_deals: int = None
    trade_volume: int = None
    trade_volume_real: int = None
    trade_turnover: int = None
    trade_interest: int = None
    trade_buy_orders: int = None
    trade_buy_volume: int = None
    trade_buy_volume_real: int = None
    trade_sell_orders: int = None
    trade_sell_volume: int = None
    trade_sell_volume_real: int = None
    price_open: float = None
    price_close: float = None
    price_change: float = None
    price_volatility: float = None
    price_theoretical: float = None

    def __str__(self):
        return self.symbol
