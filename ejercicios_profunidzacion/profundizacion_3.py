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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
temp1 = float(input('Ingrese la 1° temperatura: '))
temp2 = float(input('Ingrese la 2° temperatura: '))
temp3 = float(input('Ingrese la 3° temperatura: '))

if (temp1 > temp2) and (temp1 > temp3):
    print(f'La temperatura de {temp1} es la maxima.')
elif (temp2 > temp1) and (temp2 > temp3):
    print(f'La temperatura de {temp2} es la maxima.')
elif (temp3 > temp1) and (temp3 > temp2):
    print(f'La temperatura de {temp3} es la maxima.')

if (temp1 < temp2) and (temp1 < temp3):
    print(f'La temperatura de {temp1} es la minima.')
elif (temp2 < temp1) and (temp2 < temp3):
    print(f'La temperatura de {temp2} es la minima.')
elif (temp3 < temp1) and (temp3 < temp2):
    print(f'La temperatura de {temp3} es la minima.')

prom = (temp1 + temp2 + temp3) / 3
print(f'El promedio de temperatura es de {prom} grados.')