import pickle


class Data_save:

    def __init__(self, name_save, donnees):
        if name_save == None:
            self._name = "donnees/party.data"
        else:
            self._name = "donnees/" + name_save + ".data'"
        self._donnees = list()
        self._donnees.append(donnees)
        self.save_data()

    def set_donnees(self, name_save, donnees):
        self._name = "donnees/" + name_save + ".data'"
        self._donnees.append(donnees)

    def save_data(self):
        self._donnees = self.load_data()
        with open(self._name, "wb") as fichier:
            record = pickle.Pickler(fichier)
            record.dump(self._donnees)

    def load_data(self):
        """
			la fonction charge des donnee en fonction de la valeur de son set name

			:return: list of data de type player if self._name content the name player
		"""
        with open(self._name, "rb") as fic:
            get_data = pickle.Unpickler(fic)
            get_data = get_data.load()
        return get_data



d =Data_save(None,'hello4545')
print(d.load_data(),len(d.load_data()))
d.set_donnees("party",'ok' )
d.save_data()
print(d.load_data(),len(d.load_data()))
