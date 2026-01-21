def prvocislo(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input("Zadej celé číslo n (> 0): "))
sude = 0
liche = 0
prvocisla = 0

for i in range(1, n + 1):
    vlastnosti = []

    if i % 2 == 0:
        vlastnosti.append("sudé")
        sude += 1
    else:
        vlastnosti.append("liché")
        liche += 1
    if i % 3 == 0:
        vlastnosti.append("dělitelné 3")
    else:
        vlastnosti.append("nedělitelné 3")
    if prvocislo(i):
        vlastnosti.append("prvočíslo")
        prvocisla += 1
    else:
        vlastnosti.append("není prvočíslo")

    print(f"{i}: {', '.join(vlastnosti)}")

print("\nSouhrn:")
print(f"Sudých čísel: {sude}")
print(f"Lichých čísel: {liche}")
print(f"Prvočísel: {prvocisla}")
