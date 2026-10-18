from csv import reader

import stand_prese
from espositori import Espositori
from stand import Stand
from stand_prese import StandPrese
from stand_premium import StandPremium
from operator import attrgetter

class LingottoFiere:
    def __init__(self, nome):
        self.__nome=nome
        self.lista_espositori=[]
        self.lista_standpremium=[]
        self.lista_standprese=[]
        self.lista_stand=[]
        self.lista_codici=[]
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome=nome

    def carica_file_dati(self, file_path):
        try:
            file=open(file_path,'r')
            csv_reader = reader(file)
            for riga in csv_reader:
                if riga[0] not in self.lista_codici:
                    if riga[0].startswith('ES'):
                        codice=riga[0]
                        self.lista_codici.append(codice)
                        nome=riga[1]
                        cognome=riga[2]
                        self.lista_espositori.append(Espositori(codice,nome,cognome))
                    elif riga[0].startswith('ST'):
                        codice=riga[0]
                        self.lista_codici.append(codice)
                        superficie=riga[1]
                        padiglione=riga[2]
                        if len(riga)==5 and riga[4].isdigit():
                            prezzo=int(riga[3])
                            numero_prese=int(riga[4])
                            stand=StandPrese(codice,superficie,padiglione,prezzo,numero_prese)
                            stand.modificare_prezzo()
                            self.lista_standprese.append(stand)
                        elif len(riga)==5 and riga[4].isalpha():
                            prezzo=int(riga[3])
                            posizione=riga[4]
                            standp=StandPremium(codice,superficie,padiglione,prezzo,posizione)
                            standp.modifica_prezzo()
                            self.lista_standprese.append(standp)
                        else:
                            prezzo=int(riga[3])
                            stand=Stand(codice,superficie,padiglione,prezzo)
                            self.lista_standprese.append(stand)

        except FileNotFoundError:
            raise FileNotFoundError
        finally:
            file.close()
    def stampa_stand(self):
        for standprese in self.lista_standprese:
            print(standprese)
        for standpremium in self.lista_standpremium:
            print(standpremium)

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        if codice_stand not in self.lista_standprese:
            raise Exception('Il codice stand non esiste')
        elif codice_espositore not in self.lista_espositori:
            raise Exception('Il codice espositore non esiste')
        else:
            for espositore in self.lista_espositori:
                if espositore.codice==codice_espositore:
                    for standprese in self.lista_standprese:
                        if codice_stand==standprese.codice and espositore.stand_associati==None and standprese.espositore_associato==None:
                            espositore.aggiungi_stand_associati(standprese)
                            standprese.aggiungi_espositore(espositore)
                            break
                        elif espositore.stand_associati!=None:
                            raise Exception("L'espositore presenta già uno stand associato.")
                        elif standprese.espositore_associato!=None:
                            raise Exception("Lo stand risulta già assegnato.")




    def elenca_espositori(self):
        for espositori in self.lista_espositori:
            print(espositori)

    def stand_ordinati_per_prezzo(self):
        lista_ordinata=sorted(self.lista_standprese)
        return lista_ordinata


