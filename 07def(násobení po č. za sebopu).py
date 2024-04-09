def fact(n):
    if n < 2:
        return 1
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact
print(fact(10))