

class MT5Error(Exception):
    """
    Base error
    """
    pass


class MT5ConnectionError(MT5Error):
    """
    Connection errors
    """
    pass


class MT5SocketError(MT5Error):
    """
    Socket operations error (send, recv)
    """
    pass


class MT5RequestError(MT5Error):
    """
    Exception raised if request returned bad value
    """
    pass


class MT5ResponseError(MT5Error):
    """
    Exception for response operations
    """
    pass
