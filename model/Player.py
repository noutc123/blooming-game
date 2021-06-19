import model.Profession
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

    def __init__(self, name: str, dream):
        self._name = name
        self._dream = dream
        p = model.Profession.Profession.getProfession()
        self.prof = p
        self._fs = FinancialStatement(p)

        # position et information de la carte
        self._hasWon = False
        self._charityCount = 0

    def __str__(self):
        return f" {self._fs.salary}"

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
