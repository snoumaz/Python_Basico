"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 2a

Mostraremos el texto: "Contar letras en un texto"

Pediremos al usuario un texto, así:
"Por favor, introduzca un texto "
Puede contener números y caracteres con tilde.

A continuación mostraremos las letras que contiene y cuantas son,
ordenadas por número de apariciones. En caso de empate, en orden alfabético. 
Ignoraremos los números, los espacios y los signos de puntuación 
(punto, coma, punto y coma, exclamación, etc.)
Consideremos mayúsculas y minúsculas como la misma letra.

Por ejemplo:
"Por favor, introduzca un texto " ¿Amar?
La respuesta sería: 
"El texto contiene las letras:
a, 2 veces
m, 1 vez
r, 1 vez
"

Por ejemplo:
"Por favor, introduzca un texto " Python forever and ever
La respuesta sería: 
"El texto contiene las letras:
e, 4 veces
r, 3 veces
o, 2 veces
n, 2 veces
a, 1 vez
f, 1 vez
h, 1 vez
p, 1 vez
v, 1 vez
y, 1 vez
"

Ejercicio 2b

Mostraremos el texto: "Contar palabras en un texto"
Lo mismo que el ejercicio anterior, pero con palabras en lugar de letras.
. 
"""

texto = input("Por favor, introduzca un texto: \n") # Pedimos el texto al usuario
ignorar = " .,;:!¡¿?()[]{}\"'<>-_*/\n\t1234567890" # Variable con caracteres a ignorar

texto_limpio = "" # Variable para almacenar el texto limpio
for caracter in texto: # Recorremos cada caracter del texto
    if caracter not in ignorar: # Si el caracter no está en ignorar, lo añadimos al texto limpio
        texto_limpio += caracter.lower() # Convertimos el caracter a minúsculas

letras = [] # Lista para almacenar las letras
cantidades = [] # Lista para almacenar las cantidades


for letra in texto_limpio: # Recorremos cada letra del texto limpio
    if letra in letras: # Si la letra ya está en la lista, incrementamos su conteo
        indice = letras.index(letra) # Obtenemos el índice de la letra en la lista
        cantidades[indice] += 1 # Incrementamos el conteo
    else:
        letras.append(letra) # Añadimos la letra a la lista
        cantidades.append(1) # Añadimos el conteo

# Ordenamos por número de apariciones y luego alfabéticamente (burbuja)
for i in range(len(cantidades) - 1): # Recorremos las letras y cantidades
    for j in range(len(cantidades) - 1 - i): # Recorremos las letras y cantidades
        if cantidades[j] < cantidades[j + 1] or (cantidades[j] == cantidades[j + 1] and letras[j] > letras[j + 1]): # Si las cantidades son distintas o las cantidades son iguales y la letra anterior es mayor que la letra actual, intercambiamos
            # Intercambiar cantidades
            cantidades[j], cantidades[j + 1] = cantidades[j + 1], cantidades[j] # Intercambiar cantidades
            # Intercambiar letras
            letras[j], letras[j + 1] = letras[j + 1], letras[j] # Intercambiar letras

# Mostramos el resultado
print("\nEl texto contiene las letras:")
for i in range(len(letras)): # Mostramos cada letra y su cantidad
    print(f"{letras[i]}, {cantidades[i]} ")
