# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
pal1 = str(input('Ingrese la 1° palabra: '))
pal2 = str(input('Ingrese la 2° palabra: '))
pal3 = str(input('Ingrese la 3° palabra: '))

opc = int(input('Ingrese el num 1 para ordenar alfabeticamente. Ingrese 2 para ordenar por cantidad de letras: '))
if opc == 1:
    if pal1 > pal2 and pal1 > pal3:
        print(f'Palabra {pal1} es la mas grande')
    elif pal2 > pal1 and pal2 > pal3:
        print(f'Palabra {pal2} es la mas grande')
    elif pal3 > pal1 and pal3 > pal2:
        print(f'Palabra {pal3} es la mas grande')
    else:
        print('Error')
    
    if pal1 > pal2 and pal1 < pal3:
        print(f'Palabra {pal1} es la del medio')
    elif pal2 > pal1 and pal2 < pal3:
        print(f'Palabra {pal2} es la del medio')
    elif pal3 > pal1 and pal3 < pal2:
        print(f'Palabra {pal3} es la del medio')
    else:
        print('Error')

    if pal1 < pal2 and pal1 < pal3:
        print(f'Palabra {pal1} es la mas chica')
    elif pal2 < pal1 and pal2 < pal3:
        print(f'Palabra {pal2} es la mas chica')
    elif pal3 < pal1 and pal3 < pal2:
        print(f'Palabra {pal3} es la mas chica')
    else:
        print('Error')

elif opc == 2:
    l1 = len(pal1)
    l2 = len(pal2)
    l3 = len(pal3)
    if l1 > l2 and l1 > l3:
        print(f'La palabra {pal1} es la mas larga con {l1} letras')
    elif l2 > l1 and l2 > l3:
        print(f'La palabra {pal2} es la mas larga con {l2} letras')
    elif l3 > l1 and l3 > l2:
        print(f'La palabra {pal3} es la mas larga con {l3} letras')
    else:
        print('Son de igual tamaño')
    if l1 > l2 and l1 < l3:
        print(f'La palabra {pal1} es la intemedia con {l1} letras')
    elif l2 > l1 and l2 < l3:
        print(f'La palabra {pal2} es la intemedia con {l2} letras')
    elif l3 > l1 and l3 < l2:
        print(f'La palabra {pal3} es la intemedia con {l3} letras')
    else:
        print('Son de igual tamaño')

    if l1 < l2 and l1 < l3:
        print(f'La palabra {pal1} es la mas corta con {l1} letras')
    elif l2 < l1 and l2 < l3:
        print(f'La palabra {pal2} es la mas corta con {l2} letras')
    elif l3 < l1 and l3 < l2:
        print(f'La palabra {pal3} es la mas corta con {l3} letras')
    else:
        print('Son de igual tamaño')

else:
    print('Ingrese un valor valido.')