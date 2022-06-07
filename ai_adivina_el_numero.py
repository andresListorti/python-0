import random


def ai_adivina_el_numero(x):

    print('===========================')
    print('===========================')
    print('===========================')
    print('======Halo================')
    print('===========================')
    print('===========================')
    print(f'Selecciona un numero entre 1 y {x} para que la AI lo trate de adivinar...')

    limite_inferior = 1
    limite_superior = x

    respuesta = ''
    while respuesta != 'c':
        #generar una prediccion
        if limite_inferior!= limite_superior: 
            prediccion = random.randint(limite_inferior, limite_superior)
        else: 
            prediccion = limite_inferior

        #obtener respuesta del usuario
        respuesta = input(f'Mi prediccion es {prediccion}? \nSi es muy alta, ingresa (A). Si es baja, ingresa (B). Si es correcta, ingresa (C) ').lower()

        if respuesta == 'a':
            limite_superior = prediccion - 1
        elif respuesta == 'b':
            limite_inferior = prediccion + 1
    
    print(f'Felicidades!!! La AI adivino tu numero correctamente: {prediccion}')


ai_adivina_el_numero(10)
    

# Intervalo inicial: [1, 10]
# Prediccion: 6
# Respuesta: 'a' 
# Intervalo actualizado: [1, 5]

# Intervalo else inicial: [1, 10]
# Prediccion: 6
# Respuesta: 'b' 
# Intervalo actualizado: [7, 10]


