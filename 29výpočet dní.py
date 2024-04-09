# výpočet dní.py
# Získání vstupu od uživatele
datum1 = input("Zadejte první datum ve formátu DD.MM.RRRR: ")
datum2 = input("Zadejte druhé datum ve formátu DD.MM.RRRR: ")

# Převedení vstupu na čísla
den1, mesic1, rok1 = map(int, datum1.split('.'))
den2, mesic2, rok2 = map(int, datum2.split('.'))

# Výpočet rozdílu mezi daty
dny1 = rok1 * 365 + mesic1 * 30 + den1
dny2 = rok2 * 365 + mesic2 * 30 + den2
rozdil = abs(dny2 - dny1)

# Výpis výsledku
print(f"Mezi daty {datum1} a {datum2} je {rozdil} dní rozdílu.")