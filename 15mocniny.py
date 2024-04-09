m= int(input("Zadej mocninu:"))
e= int(input("Zadej exponent:"))
result=m
for i in range(e-1):
    result=result*m
print("Výsledek je", result,)