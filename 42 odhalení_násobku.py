cislo = int(input("Zadej číslo: "))
pocet = int(input("Zadej pocet: "))


for i in range(1,101):
    if cislo * i == pocet:
        print("Výsledek je",  i)
