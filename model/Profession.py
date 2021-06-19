
import random


class Profession:
    """
    _name
    _taxes
    _salary
    _mortgagePay
    _schoolLoanPay
    _carLoanPay
    _creditCardPay
    _otherExp
    _bankLoanPay
    _childExp
    _childExpPer
    _savings
    _mortgage
    _schoolLoans
    _carLoans
    _creditCardDebt
    """

    def __init__(self, name, salary, taxes, mortgagePay, schoolLoanPay,
                 carLoanPay, creditCardPay, otherExp, bankLoanPay, childExp, childExpPer,
                 savings, mortgage, schoolLoans, carLoans, creditCardDebt):
        self.name = name
        self._salary = salary
        self._taxes = taxes
        self._mortgagePay = mortgagePay
        self._schoolLoanPay = schoolLoanPay
        self._carLoanPay = carLoanPay
        self._creditCardPay = creditCardPay
        self._otherExp = otherExp
        self._bankLoanPay = bankLoanPay
        self._childExp = childExp
        self._childExpPer = childExpPer
        self._savings = savings
        self._mortgage = mortgage
        self._schoolLoans = schoolLoans
        self._carLoans = carLoans
        self._creditCardDebt = creditCardDebt

    def _getName(self):
        return self.name

    getName = property(_getName)

    def _getSalary(self):
        return self._salary

    getSalary = property(_getSalary)

    def _getTaxes(self):
        return self._taxes

    getTaxes = property(_getTaxes)

    def _getMortgagePay(self):
        return self._mortgagePay

    getMortgagePay = property(_getMortgagePay)

    def getSchoolLoanPay(self):
        return self._schoolLoanPay

    getSchoolLoanPay = property(getSchoolLoanPay)

    def _get_carLoanPay(self):
        return self._carLoanPay

    getcarLoanPay = property(_get_carLoanPay)

    def getCreditCardPay(self):
        return self._creditCardPay
        # p.getcarLoanPay

    getCreditCardPay = property(getCreditCardPay)

    def getOtherExp(self):
        return self._otherExp

    getOtherExp = property(getOtherExp)

    def getBankLoanPay(self):
        return self._bankLoanPay

    getBankLoanPay = property(getBankLoanPay)

    def _getChildExp(self):
        return self._childExp

    getChildExp = property(_getChildExp)

    def _getChildExpPer(self):
        return self._childExpPer

    getChildExpPer = property(_getChildExpPer)

    def getSavings(self):
        return self._savings

    def getMortgage(self):
        return self._mortgage

    def _getSchoolLoans(self):
        return self._schoolLoans

    getSchoolLoan = property(_getSchoolLoans)

    def _getCarLoans(self):
        return self._carLoans

    getCarLoans = property(_getCarLoans)

    def getCreditCardDebt(self):
        return self._creditCardDebt

    def getProfession(cls):
        Nurse = Profession("Nurse", 3100, 600, 400, 100, 100, 200, 600, 0, 0, 200, 500, 47000, 6000, 5000, 4000)

        Teacher = Profession("Teacher", 3300, 500, 500, 100, 100, 200, 700, 0, 0, 4200, 400, 50000, 12000, 5000, 4000)
        TruckDriver = Profession("TruckDriver", 2500, 500, 400, 0, 100, 100, 600,
                                 0, 0, 200, 800, 38000, 0, 4000, 3000)
        Secretary = Profession("Secretary", 2500, 500, 400, 0, 100, 100, 600, 0, 0,
                               100, 700, 38000, 0, 4000, 3000)

        Engineer = Profession("Engineer", 4900, 1000, 700, 100, 200, 200, 1000, 0, 0,
                              200, 400, 75000, 12000, 7000, 5000)

        BusinessManager = Profession("BusinessManager", 4600, 900, 700, 100, 100, 200,
                                     1000, 0, 0, 300, 400, 75000, 12000, 6000, 4000)

        AirlinePilot = Profession("AirlinePilot", 9500, 2000, 1000, 0, 300, 700, 2000,
                                  0, 0, 400, 2500, 90000, 0, 15000, 22000)

        Lawyer = Profession("Lawyer", 7500, 1800, 1100, 300, 200, 200, 1500, 0, 0, 400,
                            2000, 115000, 78000, 11000, 7000)

        PoliceOfficer = Profession("PoliceOfficer", 3000, 600, 400, 0, 100, 100, 700, 0, 0,
                                   200, 500, 46000, 0, 5000, 3000)

        Doctor = Profession("Doctor", 13200, 3200, 1900, 700, 300, 200, 2000, 0, 0, 700,
                            3500, 202000, 150000, 19000, 10000)

        Mechanic = Profession("Mechanic", 2000, 400, 300, 0, 100, 100, 400, 0, 0, 100,
                              700, 31000, 0, 3000, 3000)

        Janitor = Profession("Janitor", 1600, 300, 200, 0, 100, 100, 300, 0, 0, 100,
                             600, 20000, 0, 4000, 3000)
        profs = [Nurse, Teacher, TruckDriver, Secretary, Engineer, BusinessManager, AirlinePilot, Lawyer, PoliceOfficer,
                 Doctor, Mechanic, Janitor]
        rand = lambda n: random.randint(0, n)

        prof = profs[rand(5)]

        return prof

    getProfession = classmethod(getProfession)