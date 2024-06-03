male_pis = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
velke_pis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
cisla=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
heslo = []

import random
import string

for i in range(0, 3):
    heslo.append(random.choice(male_pis))

for i in range(0, 3):
    heslo.append(random.choice(velke_pis))

for i in range(0, 3):
    heslo.append(random.choice(cisla))  

for i in range(0, 2):
    heslo.append(random.choice(string.punctuation))



random.shuffle(heslo)
print(("").join(heslo))
