class KryziukaiNuliukai:
    def __init__(self):
        self.lenta = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.uzpildyta = set()
        self.dabar_zaidejas = "X"
        self.laimetojas = None
        self.zaidimas_vyksta = True
        self.ejimu_skaicius = 0

    def lentele(self):
        print(self.lenta[0], "|", self.lenta[1], "|", self.lenta[2])
        print("-" * 9)
        print(self.lenta[3], "|", self.lenta[4], "|", self.lenta[5])
        print("-" * 9)
        print(self.lenta[6], "|", self.lenta[7], "|", self.lenta[8])

    def zaidejas(self):
        while True:
            try:
                ivedimas = int(input(f"Žaidėjo {self.dabar_zaidejas} ėjimas, pasirinkite laukeli nuo 1 iki 9: "))
                if 1 <= ivedimas <= 9 and ivedimas not in self.uzpildyta:
                    self.lenta[ivedimas - 1] = self.dabar_zaidejas
                    self.uzpildyta.add(ivedimas)
                    self.ejimu_skaicius += 1
                    break
                else:
                    print("Klaida! Netinkamas skaičius arba laukelis jau užimtas.")
            except ValueError:
                print("Klaida! Įveskite tinkamą skaičių.")

    def kombinacijos(self):
        kombinacijos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
        for a, b, c in kombinacijos:
            if self.lenta[a] == self.lenta[b] == self.lenta[c] and self.lenta[a] == self.dabar_zaidejas:
                self.laimetojas = self.dabar_zaidejas
                return True
        return False

    def nugaletojas(self):
        if self.kombinacijos():
            self.lentele()
            print(f"Žaidimas pasibaigė per {self.ejimu_skaicius} ėjimus. Laimėtojas yra {self.laimetojas}!")
            self.zaidimas_vyksta = False
        elif self.ejimu_skaicius == 9:
            self.lentele()
            print(f"Žaidimas pasibaigė per {self.ejimu_skaicius} ėjimus. Lygiosios!")
            self.zaidimas_vyksta = False

    def kitas_zaidejas(self):
        if self.dabar_zaidejas == "X":
            self.dabar_zaidejas = "O"
        else:
            self.dabar_zaidejas = "X"

    def zaidimo_eiga(self):
        while self.zaidimas_vyksta:
            self.lentele()
            self.zaidejas()
            self.nugaletojas()
            self.kitas_zaidejas()


zaidimas = KryziukaiNuliukai()
zaidimas.zaidimo_eiga()
