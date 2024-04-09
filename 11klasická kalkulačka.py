První_číslo=int(input("Zadej první číslo"))
Druhé_číslo=int(input("Zadej druhé číslo"))
Vyber_operaci_od_1_do_4=int(input("Vyber operaci od 1 do 4 (1=+, 2=-, 3=*, 4=/)"))

if Vyber_operaci_od_1_do_4==1:
    print("Výsledek je", První_číslo+Druhé_číslo)
if  Vyber_operaci_od_1_do_4==2:
    print("Výsledek je", První_číslo-Druhé_číslo)
if Vyber_operaci_od_1_do_4==3:
    print("Výsledek je", První_číslo*Druhé_číslo)
if Vyber_operaci_od_1_do_4==4:
    print("Výsledek je", První_číslo/Druhé_číslo)