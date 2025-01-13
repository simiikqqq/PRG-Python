import random

number = random.randint(1, 10)
guess = None

while guess != number:
    guess = input("Zadej číslo (1-100): ")
    guess = int(guest)

    if guess == number:
        print("Gratuluji, uhodl jsi správné číslo:", number)
        break
    else:
        print("Neuhodl jsi správné číslo. Zkus to znovu.")
        
   
