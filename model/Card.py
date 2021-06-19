

class Card:
    _title: str
    _Description: str

    def __init__(self, title, description):
        self._title = title
        self._Description = description
    def __str__(self):
        return " titre : {} \n  Description :{}  ".format(self._title, self._Description)
    @property
    def get_card_name(self):
        return self._title

    @property
    def get_description(self):
        return self._Description


pass

"""
    IMPLEMENTATION OF THE BIGDEAL CARD AND SMALL DEALS
"""


class Oportunity_card(Card):
    _description: str
    _prix: int
    _downPayment: int
    _mortgage: int
    _cashFlowChange: int

    def __init__(self, title, description, cost, downPayment, mortgage, cashFlowChange):
        Card.__init__(self, title, description)
        self._prix = cost
        self._downPayment = downPayment
        self._mortgage = mortgage
        self._cashFlowchange = cashFlowChange

    def __str__(self):
        return " titre : {} Description :{} \n {} \n {} \n {}".format(self._title, self._Description, self._prix,
                                                                      self._downPayment, self._mortgage,
                                                                      self._cashFlowchange)

    @property
    def get_cost(self):
        return self._prix

    @property
    def get_DownPayment(self):
        return self._downPayment

    @property
    def getMortgage(self):
        return self._mortgage

    @property
    def getCashFlowChange(self):
        return self._cashFlowchange


def Opportunity():
    """
    here we create the instanciation of the opportunity cards
    """
    SD01 = Oportunity_card("Stock - ON2U Entertainment Co.",
                           "Box office hit by children's division causes record share price. "
                           + "Historic Trading Range: $10 - 30",
                           40, 0, 0, 0)
    SD02 = Oportunity_card("Stock - ON2U Entertainment Co.",
                           "Strong demand for company's library of old movies leads to good share price. "
                           + "Historic Trading Range: $10 - 30",
                           30, 0, 0, 0)
    SD03 = Oportunity_card("Stock - ON2U Entertainment Co.",
                           "New director of movie acquisitions brings revived prospects for share price. "
                           + "Historic Trading Range: $10 - 30",
                           20, 0, 0, 0)
    SD04 = Oportunity_card("Stock - ON2U Entertainment Co.",
                           "Movie buyer fired after third mega-flop! Share sink. Chairman's bonus cancelled."
                           + "Historic Trading Range: $10 - 30",
                           10, 0, 0, 0)
    SD05 = Oportunity_card("Stock - ON2U Entertainment Co.",
                           "Newest theme park is a huge flop, reports record losses. Share price hits all-time low."
                           + "Historic Trading Range: $10 - 30",
                           5, 0, 0, 0)
    SD06 = Oportunity_card("Condo for Sale - 2Br/1Ba",
                           "Parents selling 2/1 condo used by their child in college town. "
                           + "Lots of demand for rentals in this area.",
                           40000, 4000, 36000, 140)
    SD07 = Oportunity_card("Condo for Sale - 2Br/1Ba",
                           "Older 2/1 condo offered by young couple who want to move up to a 3/2 house "
                           + "due to grouwing family. Available soon.",
                           55000, 5000, 50000, 160)
    SD08 = Oportunity_card("Condo for Sale - 2Br/1Ba",
                           "Excellent 2/1 condo with many extras. Onwer wants to relocate for dream job FAST!"
                           + "She's moving up- you can too! No Cash Flow, but a possible capital gains opportunity.",
                           40000, 1000, 39000, 0)
    SD09 = Oportunity_card("Condo for Sale - 2Br/1Ba",
                           "Bank foreclosure! 2/1 condo in a desireable neighborhood. Close to jobs and stores."
                           + "Make offer, favorable financing by bank.",
                           400, 500, 3500, 2.2)
    SD10 = Oportunity_card("House for Sale - 2Br/1Ba",
                           "Nice 2/1 house aailable in a depressed market due to layoffs. Would make a good"
                           + "investment property for the right buyer.",
                           5000, 400, 4600, 2)
    SD11 = Oportunity_card("House for Sale - 2Br/1Ba",
                           "Nice 2/1 rental house suddenly available due to estate closing. Well-maintained older "
                           + "property with existing tenant.",
                           6500, 500, 6000, 1)
    SD12 = Oportunity_card("House for Sale - 2Br/1Ba",
                           "Low down payment to pick up with 2/1 house. Owner/seller unexpectedly moving out of town."
                           + " Right person will do well.",
                           5000, 300, 4700, 1)
    SD13 = Oportunity_card("House for Sale - 2Br/1Ba",
                           "2/1 house in an older area offered by the Highway Department. The market has crashed and the "
                           + "city MUST sell. No Cash Flow but a possible capital gains opportunity.",
                           3000, 100, 2900, 0)
    SD14 = Oportunity_card("House for Sale - 2Br/1Ba",
                           "Not lived in for six months, this bank-foreclosed house just reduced. Loan includes "
                           + "estimated repair costs.",
                           5000, 200, 4800, 2)
    SD15 = Oportunity_card("You Find a Great Deal!",
                           "Older 2/1 house, reposses by government agency. Ready to go with government financing "
                           + "and a tenant. Take out a loan if you must, but BUY THIS!",
                           3500, 200, 3300, 2.2)
    SD16 = Oportunity_card("You Find a Great Deal!",
                           "Company bought transferred-manager's 2/1 house. No current tenant, it has been on the market"
                           + "six months and it has just been reduced. Take out a loan if you must, but BUY THIS!",
                           4500, 0, 0, 2)
    # big deals opportunitees
    BD06 = Oportunity_card("Condo for Sale - 2Br/1Ba",
                           "Parents selling 2/1 condo used by their child in college town. "
                           + "Lots of demand for rentals in this area.",
                           40000, 4000, 36000, 140)
    BD07 = Oportunity_card("Condo for Sale - 2Br/1Ba",
                           "Older 2/1 condo offered by young couple who want to move up to a 3/2 house "
                           + "due to grouwing family. Available soon.",
                           55000, 5000, 50000, 160)
    BD08 = Oportunity_card("Condo for Sale - 2Br/1Ba",
                           "Excellent 2/1 condo with many extras. Onwer wants to relocate for dream job FAST!"
                           + "She's moving up- you can too! No Cash Flow, but a possible capital gains opportunity.",
                           40000, 1000, 39000, 0)
    BD09 = Oportunity_card("Condo for Sale - 2Br/1Ba",
                           "Bank foreclosure! 2/1 condo in a desireable neighborhood. Close to jobs and stores."
                           + "Make offer, favorable financing by bank.",
                           40000, 5000, 35000, 220)
    BD10 = Oportunity_card("House for Sale - 2Br/1Ba",
                           "Nice 2/1 house aailable in a depressed market due to layoffs. Would make a good"
                           + "investment property for the right buyer.",
                           50000, 4000, 46000, 200)
    BD11 = Oportunity_card("House for Sale - 2Br/1Ba",
                           "Nice 2/1 rental house suddenly available due to estate closing. Well-maintained older "
                           + "property with existing tenant.",
                           65000, 5000, 60000, 160)
    BD12 = Oportunity_card("House for Sale - 2Br/1Ba",
                           "Low down payment to pick up with 2/1 house. Owner/seller unexpectedly moving out of town."
                           + " Right person will do well.",
                           50000, 3000, 47000, 100)
    BD13 = Oportunity_card("House for Sale - 2Br/1Ba",
                           "2/1 house in an older area offered by the Highway Department. The market has crashed and the "
                           + "city MUST sell. No Cash Flow but a possible capital gains opportunity.",
                           30000, 1000, 29000, 0)
    BD14 = Oportunity_card("House for Sale - 2Br/1Ba",
                           "Not lived in for six months, this bank-foreclosed house just reduced. Loan includes "
                           + "estimated repair costs.",
                           50000, 2000, 48000, 200)
    BD15 = Oportunity_card("You Find a Great Deal!",
                           "Older 2/1 house, reposses by government agency. Ready to go with government financing "
                           + "and a tenant. Take out a loan if you must, but BUY THIS!",
                           35000, 2000, 33000, 220)
    BD16 = Oportunity_card("You Find a Great Deal!",
                           "Company bought transferred-manager's 2/1 house. No current tenant, it has been on the market"
                           + "six months and it has just been reduced. Take out a loan if you must, but BUY THIS!",
                           45000, 2000, 43000, 250)
    BD17 = Oportunity_card("You Find a Great Deal!",
                           "Company bought transferred-manager's 2/1 house. No current tenant, it has been on the market"
                           + "six months and it has just been reduced. Take out a loan if you must, but BUY THIS!",
                           4500, 20000, 43000, 25000)
    sdCardArray = [SD01, SD02, SD03, SD04, SD05, SD06, SD07, SD08, SD09, SD10, SD11, SD12, SD13, SD14, SD15, SD16]
    bigdCardArray = [SD01, SD02, SD03, SD04, SD05, BD06, BD07, BD08, BD09, BD10, BD11, BD12, BD13, BD14, BD15, BD16, BD17]
    return {1: sdCardArray, 2: bigdCardArray}
