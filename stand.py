class Stand:
    def __init__(self,codice,superficie,padiglione,prezzo):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo
        self.espositore_associato=None
    def aggiungi_espositore(self,espositore):
        self.espositore_associato=espositore
    @property
    def codice(self):
        return self.__codice
    @codice.setter
    def codice(self,codice):
        self.__codice = codice
    @property
    def superficie(self):
        return self.__superficie
    @superficie.setter
    def superficie(self,superficie):
        self.__superficie = superficie
    @property
    def padiglione(self):
        return self.__padiglione
    @padiglione.setter
    def padiglione(self,padiglione):
        self.__padiglione = padiglione
    @property
    def prezzo(self):
        return self.__prezzo
    @prezzo.setter
    def prezzo(self,prezzo):
        self.__prezzo = prezzo
    def __repr__(self):
        return f'{self.codice}: Standard | {self.superficie}- Padiglione: {self.padiglione} - Prezzo:{float(self.prezzo)} - Espositore associato: {self.espositore_associato}'
    def __lt__(self, other):
        return self.prezzo<other.prezzo
    def __eq__(self,other):
        if isinstance(other,Stand):
            return self.codice==other.codice
        elif isinstance(other,str):
            return self.codice==other