from stand import Stand
class StandPrese(Stand):
    def __init__(self,codice,superficie,padiglione,prezzo,numero_prese):
        super().__init__(codice,superficie,padiglione,prezzo)
        self.numero_prese = numero_prese
    def modificare_prezzo(self):
        self.prezzo = self.prezzo*(1+(0.07*self.numero_prese))
        self.prezzo=round(self.prezzo,2)

    def __repr__(self):
        return f'{super().codice}: Prese Extra | {super().superficie}- Padiglione: {super().padiglione} - Prezzo:{self.prezzo}- Prese aggiuntive: {self.numero_prese}'