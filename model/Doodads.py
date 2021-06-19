from model.Card import *
from model.Player import *

class Doodads(Card):
    def __init__(self, description, title, value):
        super(Doodads, self).__init__(title, description)
        self._value = value

    @property
    def get_Value(self):
        return self._value


    def Payer(self, Player: Player, value: float):
        """
        1 on verifie le cash si ses suffisant pour payer
        si oui alors on paye la depense
        sinon on lui demande de preter ce cash
        """
def list_Doodad():
    print("hello world")
    list_doodad=[ Doodads("Water Heater Leaks","Pay $450 for new one",450),
    Doodads("Go Out to Dinner", "Spend $80", 80),
    Doodads("New Boat! Go", "pay $1000 down and 17000$ on, time. ", 18000),
    Doodads("Buy Big Screen TV",'pay 4000$', 4000),
    Doodads("park in handicapped Zone", "pay 100$ fine", 100),
    Doodads("your birthdays", "spend 2500", 2500),
    Doodads("son's College Tuittion"," pay 1500$", 1500),
    Doodads("son's Collefe Tuitton",'pay 1500$ ', 1500),
    Doodads("buy Toys for kids","spend 50 $50",50),
    Doodads("buy Toys for your kids ", "spend 50 $",50),
    Doodads("Buy new Fishing  Rod ", " pay 100",100),
    Doodads("Play 2 Rounds of Golf ", " pay Spend $50", 50),
    Doodads("Car's Air Conditioning Dies", " pay 700", 100),
    Doodads("Tax Audit", "Pay Tax Authority $350", 100),
    Doodads("Shopping! ", " Pay $350 for fabulous fake jewels", 350),
    Doodads("Car Needs Tires", " pay 100", 100),
    Doodads("Buy new Fishing  Rod ", " Pay $300",300),
    Doodads("New Boat! Go", "Spend $80", 80),
    Doodads("New Boat! Go", "Spend $80", 80),
    Doodads("New Boat! Go", "Spend $80", 80),
    Doodads("New Boat! Go", "Spend $80", 80),
    Doodads("New Boat! Go", "Spend $80", 80),
    Doodads("New Boat! Go", "Spend $80", 80)]
    for i in range(1 , len(list_doodad)-1):
        print(list_doodad[i])
    pass