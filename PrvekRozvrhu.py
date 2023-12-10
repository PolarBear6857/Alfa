from Predmet import Predmet
from Trida import Trida
from Ucitel import Ucitel


class PrvekRozvrhu:
    def __init__(self, predmet, ucitel, trida):
        if isinstance(predmet, Predmet) and isinstance(ucitel, Ucitel) and isinstance(trida, Trida):
            self.predmet = predmet
            self.ucitel = ucitel
            self.trida = trida

    def __str__(self):
        return "Předmět: " + self.predmet.nazev + ", Učitel: " + self.ucitel.jmeno + " " + self.ucitel.prijmeni + ", Třída: " + self.trida.cislo
