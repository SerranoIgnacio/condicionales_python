# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

pal1 = len(texto_1)
pal2 = len(texto_2)
if pal1 > pal2:
    print('La primera palabra es mayor')
elif pal2 > pal1:
    print('La segunda palabra es mayor')
else:
    print('Las palabras son iguales.')

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

pal1 = len(texto_1)
pal2 = len(texto_2)
if pal1 > pal2:
    print(f'La palabra tiene {pal1} letras')
elif pal2 > pal1:
    print(f'La palabra tiene {pal2} letras')
else:
    print(f'Las palabras son iguales. Palabra_1 tiene {pal1} letras y palabra_2 tiene tambien {pal2} letras')

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
t1 = texto_1[0]
t2 = texto_2[0]
if t1 > t2:
    print(f'La letra {t1} es mayor que {t2}')
else:
    print(f'La letra {t2} es mayor que {t1}')

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1:
    print(f'La variable es igual!')

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 != texto_2:
    print(f'La variables son diferentes!')
else:
    print('las variables son iguales.')
