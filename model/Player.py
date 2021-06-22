from model.Profession import Profession
import model.FinancialStatement
from model.FinancialStatement import *


class Player:
    _fs: FinancialStatement
    """
    _charityCount;  #charity counter
    _downsizeCount; #down size counter
    _location;
    _hasWon;
    """

    def __init__(self, name):
        self._name = name
        self._dream = None
        self.prof = Profession.getProfession()
        self._fs = FinancialStatement(self.prof)

        # position et information de la carte
        self._hasWon = False
        self._charityCount = 0

    def show(self):
        l=[self.prof._getName, self._fs.salary,self._fs.getCashBalance]
        return

    @property
    def get_name(self):
        return self._name

    @property
    def gethaswon(self):
        return self._hasWon

    @property
    def get_finance(self):
        return self._fs

    def get_charity(self):
        return self._charityCount

    def _setcharity(self, number):
        self._charityCount = number

    CharityCount: property = property(get_charity, _setcharity)
