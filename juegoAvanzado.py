import random
nivel_sencillo = (0,100)
nivel_medio = (0,1000)
nivel_avanzado = (0, 1000000)
nivel_experto = (0,1000000000000)
game_levels = ["nivel_sencillo:" + str(nivel_sencillo), "nivel_medio:" + str(nivel_medio), "nivel_avanzado:" + str(nivel_avanzado), "nivel_experto:" + str(nivel_experto)]
print(game_levels)
user = input("Choose one level for the game:")
print(user)
while user == nivel_sencillo:
    import random
    nivel_sencillo = random.randint(0,100)
    print(nivel_sencillo)
    print("Choose an integer between 0 and 99")
    intento_1 = int(input())
    while intento_1 != nivel_sencillo:
        
    
    
nivel_medio = random.randint(0,1000)
nivel_avanzado = random.randint(0, 1000000)
nivel_experto = random.randint(0,1000000000000)

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
     
