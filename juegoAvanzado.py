nivel_sencillo = 0
nivel_medio = 1
nivel_avanzado = 2
nivel_experto = 3
game_levels = ["Game levels:" + "nivel_sencillo:" + str(nivel_sencillo), "nivel_medio:" + str(nivel_medio), "nivel_avanzado:" + str(nivel_avanzado), "nivel_experto:" + str(nivel_experto)]
print(game_levels)
user = int(input("Choose one level for the game:"))

if user == 0:
    import random
    number = random.randint(0,100)
    print(number)
    print("Choose an integrer between 0 and 99")
    intento_1 = int(input())
    while intento_1 != number:
        if intento_1 > 99:
            print("Choose another number between 0 an 99")
        else:
            if intento_1 > number:
                print("Too far from the number, it's smaller. The number is between:" + "0 y" + str(intento_1))
            else:
                print("Too far from the number, it's bigger. The number is between:" + str(intento_1) + "y 99")
        intento_1 = int(input())
    if intento_1 == number:
        print("¡Congratulations!, you have completed level 0")

if user == 1:
    import random
    number = random.randint(0,1000)
    print(number)
    print("Choose an integrer between 0 and 1000")
    intento_1 = int(input())
    while intento_1 != number:
        if intento_1 > 999:
            print("Choose another number between 0 an 999")
        else:
            if intento_1 > number:
                print("Too far from the number, it's smaller. The number is between:" + "0 y" + str(intento_1))
            else:
                print("Too far from the number, it's bigger. The number is between:" + str(intento_1) + "y 999")
        intento_1 = int(input())
    if intento_1 == number:
        print("¡Congratulations!, you have completed level 1")

if user == 2:
    import random
    number = random.randint(0,1000000)
    print(number)
    print("Choose an integrer between 0 and 1000000")
    intento_1 = int(input())
    while intento_1 != number:
        if intento_1 > 999999:
            print("Choose another number between 0 an 999999")
        else:
            if intento_1 > number:
                print("Too far from the number, it's smaller. The number is between:" + "0 y " + str(intento_1))
            else:
                print("Too far from the number, it's bigger. The number is between:" + str(intento_1) + "y 999999")
        intento_1 = int(input())
    if intento_1 == number:
        print("¡Congratulations!, you have completed level 2")

if user == 3:
    import random
    number = random.randint(0,1000000000000)
    print(number)
    print("Choose an integrer between 0 and 1000000000000")
    intento_1 = int(input())
    while intento_1 != number:
        if intento_1 > 999999999999:
            print("Choose another number between 0 an 999999999999")
        else:
            if intento_1 > number:
                print("Too far from the number, it's smaller. The number is between:" + "0 y" + str(intento_1))
            else:
                print("Too far from the number, it's bigger. The number is between:" + str(intento_1) + "y 999999999999")
        intento_1 = int(input())
    if intento_1 == number:
        print("¡Congratulations!, you have completed level 3")

