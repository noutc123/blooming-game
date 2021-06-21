
class FinancialStatement:
    """
    self._profession =profession()
    self._cashBalance
    #income
    self._income
    self._salary
    self._REcashFlow
    #Expenses
    self._expenses #besoin de getter et d incrementater
    self._taxes
    self._homeMortgagePayment
    self._schoolLoanPayment
    self._carLoanPayment
    self._creditCardPayment
    self._otherExpenses
    self._perChildExpense
    self._numChildren
    #besoin des # Assets
    self._assets
    self._savings
    self._stock
    self._realEstate = list()

    # Liabilities
    self._liabilities
    self._homeMortgage
    self._schoolLoans
    self._carLoans
    _creditCardDebt

    # Cash flows (top right of actual financial statement)
    _monthlySalary
    _passiveIncome
    _totalIncome
    _totalExpenses
    _monthlyCashFlow
    _hasWon
    """

    def __init__(self, p):
        self._profession = p
        # income
        self._income = 0.00
        self._salary = p.getSalary
        self._REcashFlow = 0.00
        # Expenses
        self._cashBalance = 0.0
        self._expenses = 0  # besoin de getter et d incrementater
        self._taxes = p.getTaxes
        self._homeMortgagePayment = p.getMortgagePay
        self._schoolLoanPayment = p.getSchoolLoanPay
        self._carLoanPayment = p.getcarLoanPay
        self._creditCardPayment = p.getCreditCardPay
        self._otherExpenses = p.getOtherExp
        self._perChildExpense = p._childExpPer

        # besoin des
        # Assets
        self._assets = 0
        self._savings = p.getSavings()
        self._stock = None
        self._realEstate = list()

        # Liabilities
        self._liabilities = 0
        self._homeMortgage = p.getMortgage()
        self._schoolLoans = p.getSchoolLoan
        self._carLoans = p.getCarLoans
        self._creditCardDebt = p.getCreditCardDebt()
        self._numChildren = 0
        # Cash flows (top right of actual financial statement)
        self._monthlySalary = self._salary
        self._passiveIncome = 0.0
        self._totalIncome = 0
        self._totalExpenses = 0
        self._monthlyCashFlow = 0
        self._hasWon = False
        self.update()

    def update(self):
        self._income = self._salary + self._REcashFlow
        self._totalExpenses = self._taxes + self._homeMortgagePayment + self._schoolLoanPayment + self._carLoanPayment + self._creditCardPayment + self._otherExpenses + self._perChildExpense * self._numChildren
        self._assets =0 # self.getOwnedREValue() + self.getStockValue() + self._savings
        self._liabilities = self._homeMortgage + self._schoolLoans + self._carLoans + self._creditCardDebt
        self._cashBalance = self._salary - self._totalExpenses
        self._passiveIncome = self.getPassiveIncome
        self._totalIncome = self._monthlySalary + self._passiveIncome

        self._monthlyCashFlow = self._totalIncome - self._totalExpenses
        self._hasWon = self._passiveIncome > self._totalExpenses

    @property
    def getPassiveIncome(self):

        for re in self._realEstate:
            self._passiveIncome += re.getCashFlow()

        return self._passiveIncome

    @property
    def getStockValue(self):
        if (self._stock == None):
            return 0
        else:
            return self._stock.getNumShares() * self._stock.getSharePrice()

    @property
    def getOwnedREValue(self):
        reValue = 0
        i = 0
        for i in range(len(self._realEstate) - 1):
            reValue = self._realEstate[i]
            pricevalue =+ reValue.getPrice
        return reValue

    @property
    def canBuy(self, price) -> bool:
        if price < self._cashBalance:
            return True
        return False
    @property
    def hasStock(self):
        if self._stock != None :
            return True
        return False

    @property
    def getCashBalance(self):
        return self._cashBalance

    def getCashBalance(self, valuer: int):
        self._cashBalance = valuer

    """
    def buyProperty( newProperty ):
        self._cashBalance -= newProperty.getDownPayment()
        self._realEstate.add(newProperty)
        self.update()
    
    def buyStock(self,numShares,sharePrice):
        self._stock =  Stock(numShares, sharePrice)
            cashOut = self._stock.getCashOut()
        self._cashBalance += cashOut	# getCashOut() will negate the value automatically so we will add not subtract
        self.update()
    """

    @property
    def sellStock(self):
        self._cashBalance += self._stock.getSharePrice() * self._stock.getNumShares()
        self._stock = None
        self.update()

    @property
    def addChild(self):

        # People can only have a max of 3 children
        if(self._numChildren < 3):

            self._numChildren =+1

        self.update()

    @property
    def increaseCashBalance(self, cashIncrease):

        self._cashBalance =+ cashIncrease
        self.update()

    @property
    def getProfession(self):
        return self._profession

    @property
    def salary(self):
        return self._salary
