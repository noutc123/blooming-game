import random


class Dice:
    def __init__(self, value=1):
        self._value = value

    def setdice(self, Val):
        # modifie la valeur du de en fonction la carte charity
        self._value = Val
    def getdice(self):
        return  self._value
    def roll(self):
        """
            fonction pour lancer le dee elle prende trois la valuer du dee parametre et retourne un de en fonction de cette
            valeur
        """
        if self._value == 1:
            return 1, random.randint(1, 6)
        elif self._value == 2:

            return 1, random.randint(1, 6), random.randint(1, 6)
        else:

            return 3, random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

"""
test des class
roll = Dice()
print(roll.roll())
roll.setdice(1)
print(roll.roll())
roll.setdice(3)
print(roll.roll())
"""