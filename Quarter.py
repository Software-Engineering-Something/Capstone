from Assets import Assets
from CaceCarryValue import CaceCarryValue
from CacePeriodFlux import CacePeriodFlux
from FinalRevenue import FinalRevenue
from IncomeB4Taxes import IncomeB4Taxes
from NetIncome import NetIncome
from TotalEquity import TotalEquity
from TotalLiabilityEquity import TotalLiabilityEquity


class Quarter:
    """Objects of each data held within a quarter"""
    assets = Assets()
    cace_carryValue = CaceCarryValue()
    cace_periodFlux = CacePeriodFlux()
    finalRevenue = FinalRevenue()
    incomeB4taxes = IncomeB4Taxes()
    netIncome = NetIncome()
    totalEquity = TotalEquity()
    totalLiabilityEquity = TotalLiabilityEquity()

    """Constructor allows for built in getter and setter of quarter"""
    def __init__(self, quarter):
        self.quarter = quarter

