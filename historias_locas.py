# Concatenar cadenas de caracteres 
# supongamos que queremos crear una cadena que diga:
# Apreden a programar con _______.

# organizacion = 'freeCodeCamp'

# print('Aprende a Programar con ' + organizacion)
# print('Aprende a programar con {}'.format(organizacion))
# print(f'Aprende a programar con {organizacion}') # f-string

#  Mad Libs - historias locas


adj = input('Ingrese Adjetivo: ')
verbo1 = input('Ingrese Verbo A: ')
verbo2 = input('Ingrese Verbo B: ')
sustantivo_plural = input('Ingrese Sustantivo plural: ')


madLib = f'Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1}. Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!'

print(madLib)