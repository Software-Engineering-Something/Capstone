class Company:
    """Class level list holds year objects"""
    years = []

    """Constructor allows for built in getter and setter for parameters"""
    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker

