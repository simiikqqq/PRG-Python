def CaesarSifra(text, posun):
    za = ord('a')
    zA = ord('A')
    z = ord('z')
    zZ = ord('Z')
    result = ""
    
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - za + posun) % 26 + za)
            elif char.isupper():
                result += chr((ord(char) - zA + posun) % 26 + zA)
        else:
            result += char
    
    return result

# Testování funkce
text = "Dobry den!"
posun = 5
zasifrovany_text = CaesarSifra(text, posun)
print("Zašifrovaný text:", zasifrovany_text)

desifrovany_text = CaesarSifra(zasifrovany_text, -posun)
print("Dešifrovaný text:", desifrovany_text)