from Card import Card
from DATA import data_access

class Dream(Card):
    """
     ===================================================================================================================
     =                                                                                                                 =
     = this class who have the dream of the player we can create it an push it on the databases accees who name DREAMS =
     =                                                                                                                 =
     ===================================================================================================================
     :Authors:
     :Authors:


     :return
    """
    def __init__(self, title, description, price:int):
        Card.__init__(self, title, description)
        self._price = price

    def __str__(self):
        return f"{self._title}, {self._Description}, {self._price}"

    def set_price(self, value):
        if value:
            self._price *= self._price


"""

il faut pucher les reve dans la bd binaire
1 cree la methode qui vas retourner un liste de reve et appeler la classe reve qui feras le travail 
"""

d = Dream(" dineer ",  "Votre rêve est d'être un chef d'entreprise. Tu créés ton entreprise et tu es le chef laba.", 2000000)