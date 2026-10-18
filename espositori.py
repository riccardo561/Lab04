from stand import Stand
class Espositori:
    def __init__(self,codice,nome,cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome
        self.stand_associati=None
    def aggiungi_stand_associati(self,stand):
        self.stand_associati=stand.codice

    @property
    def codice(self):
        return self.__codice
    @codice.setter
    def codice(self,codice):
        self.__codice = codice
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    @property
    def cognome(self):
        return self.__cognome
    @cognome.setter
    def cognome(self,cognome):
        self.__cognome = cognome
    def __repr__(self):
        return f'{self.__codice} - Nome: {self.__nome} - Cognome: {self.cognome}, Stand Associati: {self.stand_associati}'
    def __eq__(self,other):
        if isinstance(other,Espositori):
            return self.codice == other.codice
        elif isinstance(other,str):
            return self.codice == other