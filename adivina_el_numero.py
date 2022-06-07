import random # asi se importa el modulo random de python



def adivina_el_numero(x): 
    print('=============================')
    print('  Bienvenido al Juego!       ')
    print('=============================')
    print('Tu meta es adivinar el numero generado por la computadora.')

    numero_aleatorio = random.randint(1, x) #random integral entre 1 y x

    prediccion = 0

    while prediccion != numero_aleatorio:
        #usuario ingresa numero
        prediccion = int(input(f'Ingrese su prediccion entre 1 y {x}: ')) #esto se llama f-string #luego int te pasa la cadena a numero entero #input siempre te va a mandar un string
        if prediccion < numero_aleatorio:
            print('Intenta de nuevo, tu numero es bajo')
        elif prediccion > numero_aleatorio:
            print('Intenta de nuevo, tu numero fue grande')
    
    print(f'Felicidades! ---- Adivinaste el {numero_aleatorio} correctamente!!!!!!!!!!!!!')

#la sangria marca el ambito

#tiene que haber 2 lineas en blanco entre la definicion d ela funcion y cualquier otra cosa- recomienda la guia de estilo de pyton

adivina_el_numero(10)

