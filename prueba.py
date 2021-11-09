user = int(input("Choose one level for the game:"))
while user == 1:
    if user == 1:
        import random
        numero = random.randint(0,100)
        print(numero)
        print("Choose an integer between 0 and 99")
        intento_1 = int(input())