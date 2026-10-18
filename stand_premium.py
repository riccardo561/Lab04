from stand import Stand
class StandPremium(Stand):
    def __init__(self,codice,superficie,padiglione,prezzo,posizione):
        super().__init__(codice,superficie,padiglione,prezzo)
        self.posizione = posizione
    def modifica_prezzo(self):
        self.prezzo = self.prezzo*(1.30)
        self.prezzo=round(self.prezzo,2)
    def __repr__(self):
        return f'{super().codice}: Premium | {super().superficie} -Prezzo:{self.prezzo} - Padiglione: {super().padiglione} - Lato in posizione: {self.posizione}'

