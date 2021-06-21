import pickle


class Data_save:

    def __init__(self, name_save, donnees):
        if name_save == None:
            self._name = "donnees/party.data"
        else:
            self._name = "../DATA/donnees/" + name_save + ".data'"
        self._donnees = list()
        self._donnees.append(donnees)
        self.save_data()

    def set_donnees(self, name_save, donnees):
        self._name = "donnees/" + name_save + ".data'"
        self._donnees.extend(donnees)
    def resave_data(self):
        self._donnees.extend( self.load_data())
        with open(self._name, "wb") as fichier:
            record = pickle.Pickler(fichier)
            record.dump(self._donnees)

    def save_data(self):
        with open(self._name, "ab") as fichier:
            record = pickle.Pickler(fichier)
            record.dump(self._donnees)

    def load_data(self):
        """
			la fonction charge des donnee en fonction de la valeur de son set name

			:return: list of data de type player if self._name content the name player
        """
        with open(self._name, "ab") as fic:
            get_data = pickle.Unpickler(fic)
            get_data = get_data.load()
        return get_data

list_race = [(400,440,16,16),(380,400,16,16),(370,360,16,16),(360,310,16,16),
                 (370,270,16,16),(400,230,16,16),(430,190,16,16),(480,180,16,16),(520,160,16,16),
                 (570,170,16,16),(620,180,16,16),(660,200,16,16),(700,230,16,16),(720,270,16,16),(740,310,16,16),(740,360,16,16),(720,400,16,16),
                 (700,440,16,16),(660,470,16,16),(620,490,16,16),(570,500,16,16),(530,510,16,16),(480,490,16,16),(440,470,16,16)]
list_race1 = [(120, 580, 16, 16), (110, 520, 16, 16), (110, 460, 16, 16), (110, 400, 16, 16),
             (110, 330, 16, 16), (110, 280, 16, 16), (110, 220, 16, 16), (110, 160, 16, 16),
              (130, 100, 16, 16),
             (190, 90, 16, 16), (260, 90, 16, 16), (330, 90, 16, 16), (400, 90, 16, 16), (470, 90, 16, 16),
             (540, 90, 16, 16), (610, 90, 16, 16), (680, 90, 16, 16),
             (750, 90, 16, 16), (830, 90, 16, 16), (910, 90, 16, 16), (980, 90, 16, 16),
              (980, 150, 16, 16),
             (980, 220, 16, 16), (980, 280, 16, 16), (980, 340, 16, 16), (980, 400, 16, 16)
              , (980, 460, 16, 16), (980, 520, 16, 16), (980, 580, 16, 16), (910, 580, 16, 16)
              , (830,580, 16, 16), (750, 580, 16, 16), (680, 580, 16, 16), (610, 580, 16, 16),
              (540,580, 16, 16),(470,580, 16, 16),(400,580, 16, 16),(330,580, 16, 16),
              (260,580, 16, 16),(190,580, 16, 16),(190,580, 16, 16) ]
d = Data_save("player_position", [list_race,list_race1])
