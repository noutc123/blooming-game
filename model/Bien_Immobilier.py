
class Propriete:
    def __init__(self, name, price, monthvers, cashflow):
        self._name = name
        self._price = price
        self._versement = monthvers
        self._cashFlow = cashflow
    @property
    def Name(self):
        return self._name