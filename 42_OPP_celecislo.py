class CeleCislo:

    def __init__(self, cele_cislo):
        self.cislo = cele_cislo
    
    def je_prirozene(self):
        return self.cislo > 0
    
    def je_prvocislo(self):
        if self.cislo <= 1:
            return False
        for i in range (2, int(self.cislo ** 0.5 + 1)):
            if self.cislo % i == 0:
                return False
        return True

    def __str__(self):
        prirozene = "je" if self.je_prirozene() else "neni"
        prvocislo = "je" if self.je_prvocislo() else "neni"
        return f"{self.cislo} {prirozene} přirozené a {prvocislo} prvočíslo."
    

cisla = [-11, -1, 0, 5, 27, 29,]

for c in cisla:
    cele_cislo = CeleCislo(c)
    print(cele_cislo)
