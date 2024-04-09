import random

def get_user_choice():
    user_choice = input("Vyber kámen, papir, nebo nůžky: ").lower()
    while user_choice not in ['kámen', 'papir', 'nůžky']:
        print("Nesprávné volba. Zadejte kámen, papir nebo nůžky.")
        user_choice = input("Vyber kámen, papir, nebo nůžky:").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['kámen', 'papir', 'nůžky'])

user_choice = get_user_choice()
computer_choice = get_computer_choice()

print("Hráč:", user_choice)
print("Počítač:", computer_choice)

if user_choice == computer_choice:
    print("Nikdo nevyhrál")
elif user_choice == 'kámen':
    if computer_choice == 'papir':
        print("Počítač vyhrál")
    else:
        print("Hráč vyhrál")
elif user_choice == 'papir':
    if computer_choice == 'nůžky':
        print("Počítač vyhrál")
    else:
        print("Hráč vyhrál")
elif user_choice == 'nůžky':
    if computer_choice == 'kámen':
        print("Počítač vyhrál")
    else:
        print("Hráč vyhrál")