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

    
   # if user == 0:
    #    import random
    #numero = random.randint(0,100)
    #print(numero)
    #print("Choose an integer between 0 and 99")
    #intento_1 = int(input())
    
    

    
        
    
    
#nivel_medio = random.randint(0,1000)
#nivel_avanzado = random.randint(0, 1000000)
#nivel_experto = random.randint(0,1000000000000)

#print(numero)
# print("Intento is an integer")
# intento_1 = int(input())
# while intento_1 != numero:
    
    #if intento_1 > 99:
        #print("Choose another number between 0 an 99")
    #else:
     #   if intento_1 > numero:
      #      print("Too far from the number, it's smaller. The number is between:" + "0 y" + str(intento_1))
       # else:
        #    print("Too far from the number, it's bigger. The number is between:" + str(intento_1) + "y 99")
    #intento_1 = int(input())
#if intento_1 == numero:
 #    print("¡Congratulations!")
