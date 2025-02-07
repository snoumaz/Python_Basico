"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 3
Un anagrama es un texto o palabra resultante de modificar el orden de otro texto o palabra.
Los textos deberán ir sin tildes (acentos o diéresis)
No se tienen en cuenta mayúsculas ni espacios.

Mostraremos el mensaje: "Anagramas"
Pediremos al usuario un texto/palabra.
Pediremos al usuario un segundo texto/palabra
Responderemos si ambos son anagramas o no.

Por ejemplo:
    "Introduzca el primer texto --> " Pedro
    "Introduzca el segundo texto --> " Poder
    "Son anagramas --> Sí"

Otro ejemplo:
    "Introduzca el primer texto --> " Ramon
    "Introduzca el segundo texto --> " Morir
    "Son anagramas --> No"
 
"""
print("Anagramas")

# Pedir los textos al usuario
texto1 = input("Introduzca el primer texto --> ").lower()
texto2 = input("Introduzca el segundo texto --> ").lower()

# Eliminar tildes manualmente y caracteres no alfabéticos
texto1_limpio = ""
for caracter in texto1:
    if caracter == 'á':
        texto1_limpio += 'a'
    elif caracter == 'é':
        texto1_limpio += 'e'
    elif caracter == 'í':
        texto1_limpio += 'i'
    elif caracter == 'ó':
        texto1_limpio += 'o'
    elif caracter == 'ú' or caracter == 'ü':
        texto1_limpio += 'u'
    elif 'a' <= caracter <= 'z':  # Solo letras
        texto1_limpio += caracter

texto2_limpio = ""
for caracter in texto2:
    if caracter == 'á':
        texto2_limpio += 'a'
    elif caracter == 'é':
        texto2_limpio += 'e'
    elif caracter == 'í':
        texto2_limpio += 'i'
    elif caracter == 'ó':
        texto2_limpio += 'o'
    elif caracter == 'ú' or caracter == 'ü':
        texto2_limpio += 'u'
    elif 'a' <= caracter <= 'z':  # Solo letras
        texto2_limpio += caracter

# Verificar si tienen la misma longitud
if len(texto1_limpio) != len(texto2_limpio):
    print("Son anagramas --> No")
else:
    # Convertir a listas
    lista_texto1 = list(texto1_limpio)
    lista_texto2 = list(texto2_limpio)

    
    indice_actual = 0
    while indice_actual < len(lista_texto1):
        indice_comparacion = indice_actual + 1
        while indice_comparacion < len(lista_texto1):
            if lista_texto1[indice_actual] > lista_texto1[indice_comparacion]:
                temp = lista_texto1[indice_actual]
                lista_texto1[indice_actual] = lista_texto1[indice_comparacion]
                lista_texto1[indice_comparacion] = temp
            if lista_texto2[indice_actual] > lista_texto2[indice_comparacion]:
                temp = lista_texto2[indice_actual]
                lista_texto2[indice_actual] = lista_texto2[indice_comparacion]
                lista_texto2[indice_comparacion] = temp
            indice_comparacion += 1
        indice_actual += 1

    # Comparar listas ordenadas
    if lista_texto1 == lista_texto2:
        print("Son anagramas --> Sí")
    else:
        print("Son anagramas --> No")
