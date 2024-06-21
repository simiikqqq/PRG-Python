def kalkulacka (a, b, operace = ""):
    if operace == "+":
        return a + b
    if operace == "-":
        return a - b
    if operace == "*":
        return a * b
    if operace == "/":
        return a / b
    
print(kalkulacka(1, 2, "/"))
    
