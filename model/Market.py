#!/usr/bin/python3
#coding:utf-8
import random
from model.Bien_Immobilier import *
from model.Player import *
from model.Card import *



def getMarket_list():

        REPercent1 =  Market_card("House Buyer - 3BR/2BA",
        "Buyer searching for 3Br/2Ba house. Offers your original cost plus 10%. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "repercent",110,"3Br2Ba")
        REPercent2 =  Market_card("House Buyer - 2BR/1BA",
        "Buyer looking to aquire 2Br/1Ba rentals. Offers your original cost plus 10%. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "repercent",110,"2Br1Ba")
        REPercent3 =  Market_card("House Buyer - 3BR/2BA",
        "Buyer searching for 3Br/2Ba house. Offers your original cost plus 20%. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "repercent",120,"3Br2Ba")
        REPercent4 =  Market_card("House Buyer - 2BR/1BA",
        "Buyer looking to aquire 2Br/1Ba rentals. Offers your original cost plus 20%. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "repercent",120,"2Br1Ba")
        REPercent5 =  Market_card("House Buyer - 3BR/2BA",
        "Buyer searching for 3Br/2Ba house. Offers your original cost plus 15%. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "repercent",115,"3Br2Ba")
        REPercent6 =  Market_card("Plex Buyer",
        "Buyer looking for all Apartment and Plexes in any combination of units. Offers your original cost plus 10%. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "repercent",110,"plex")
        REPercent7 =  Market_card("Plex Buyer",
        "Buyer looking for all Apartment and Plexes in any combination of units. Offers your original cost plus 5%. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "repercent",105,"plex")
        REPercent8 =  Market_card("Plex Buyer",
        "Buyer looking for all Apartment and Plexes in any combination of units. Offers your original cost plus 15%. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "repercent",115,"plex")
        REPercent9 =  Market_card("Plex Buyer",
        "Buyer looking for all Apartment and Plexes in any combination of units. Offers your original cost plus 20%. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "repercent",120,"plex")


        REFixed1 =  Market_card("House Buyer - 3BR/2BA",
        "Buyer searching for 3Br/2Ba house. Offers your original cost plus $15,000. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "refixed",15000,"3Br2Ba")
        REFixed2 =  Market_card("House Buyer - 3BR/2BA",
        "Buyer searching for 3Br/2Ba house. Offers your original cost plus $10,000. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "refixed",10000,"3Br2Ba")
        REFixed3 =  Market_card("House Buyer - 3BR/2BA",
        "Buyer searching for 3Br/2Ba house. Offers your original cost plus $20,000. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "refixed",20000,"3Br2Ba")
        REFixed4 =  Market_card("House Buyer - 3BR/2BA",
        "Buyer searching for 3Br/2Ba house. Offers your original cost plus $5,000. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "refixed",5000,"3Br2Ba")
        REFixed5 =  Market_card("Plex Buyer",
        "Buyer looking for all Apartment and Plexes in any combination of units. Offers your original cost plus $1,000. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "refixed",1000,"plex")
        REFixed6 =  Market_card("Plex Buyer",
        "Buyer looking for all Apartment and Plexes in any combination of units. Offers your original cost plus $30,000. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "refixed",30000,"plex")
        REFixed7 =  Market_card("Plex Buyer",
        "Buyer looking for all Apartment and Plexes in any combination of units. Offers your original cost plus $15,000. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "refixed",15000,"plex")
        REFixed8 =  Market_card("Plex Buyer",
        "Buyer looking for all Apartment and Plexes in any combination of units. Offers your original cost plus $5,000. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "refixed",5000,"Plex")
        REFixed9 =  Market_card("Plex Buyer",
        "Buyer looking for all Apartment and Plexes in any combination of units. Offers your original cost plus $1,000. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "refixed",1000,"Plex")
        REFixed10 =  Market_card("Plex Buyer",
        "Buyer looking for all Apartment and Plexes in any combination of units. Offers your original cost plus $20,000. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "refixed",20000,"Plex")
        REFixed11 =  Market_card("Plex Buyer",
        "Buyer looking for all Apartment and Plexes in any combination of units. Offers your original cost plus $10,000. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "refixed",10000,"Plex")

        REHOffer1 =  Market_card("House or Condo Buyer - 2BR/1BA",
        "You are offered $45,000 for a 2Br/1Ba House or Condo. Buyer has their own financing. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "hoffer",45000,"2Br1Ba")
        REHOffer2 =  Market_card("House or Condo Buyer - 2BR/1BA",
        "You are offered $65,000 for a 2Br/1Ba House or Condo. Buyer has their own financing. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "hoffer",65000,"2Br1Ba")
        REAOffer1 =  Market_card("Apartment House Buyer",
        "Buyer offers $25,000 per unit for all units in apartment houses of any size. (His 1031 tax-deferred exchange time is running out.) Buyer has their own financing. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "aoffer",25000,"Plex")
        REAOffer2 =  Market_card("Apartment House Buyer",
        "Buyer offers $45,000 per unit for all units in apartment houses of any size. (His 1031 tax-deferred exchange time is running out.) Buyer has their own financing. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "aoffer",45000,"Plex")
        REAOffer3 =  Market_card("Apartment House Buyer",
        "REIT offers $30,000 per unit for all units in apartment houses of 12 units or more. Buyer has capital from the sale of another apartment complex. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "aoffer",30000,"Plex")
        REAOffer4 =  Market_card("Apartment House Buyer",
        "REIT offers $40,000 per unit for all units in apartment houses of 12 units or more. Buyer has capital from the sale of another apartment complex. Everyone may sell any number of properties at this price. If you sell, pay off the related mortgage and give up the cash flow on this property.",
        "aoffer",40000,"Plex")
        marketCardArray = [REPercent1, REPercent2, REPercent3, REPercent4, REPercent5, REPercent6, REPercent7, REPercent8, REPercent9,REFixed1, REFixed2, REFixed3, REFixed4, REFixed5, REFixed6, REFixed7, REFixed8, REFixed9, REFixed10, REFixed11,REHOffer1, REHOffer2,REAOffer1, REAOffer2, REAOffer3, REAOffer4]
        Valeur=len(marketCardArray)-1
        rand=lambda n:random.randint(0,n)
        Market_card1= marketCardArray[rand(Valeur)]

        return Market_card1


class Market_card(Card) :

    def __init__(self,title,description,price,Ide, Type):
       Card.__init__(self,title,description)
       self._price = price
       self._id = Ide
       self._type = Type
    def __str__(self):
        return " {}  \n  {}  \n  {}  \n {} \n {} ".format(self._title ,self._Description , self._price ,
       self._id ,
       self._type )
    @property
    def buyProperty(self, newProperty: Propriete , player: Player):
        self._cashBalance -= newProperty._versement
        self._realEstate.add(newProperty)
        player._fs.update()
        pass











