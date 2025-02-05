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

texto1 = input("Introduzca el primer texto --> ") # Pedimos al usuario un texto/palabra
texto2 = input("Introduzca el segundo texto --> ") # Pedimos al usuario un segundo texto/palabra

texto1 = texto1.lower() # Convertimos el texto a minúsculas sin tildes
texto2 = texto2.lower() # Convertimos el texto a minúsculas sin tildes

texto1 = ''.join(c for c in texto1 if c.isalnum()) # Eliminamos los caracteres que no sean alfanuméricos y convertimos el texto a minúsculas sin tildes
texto2 = ''.join(c for c in texto2 if c.isalnum()) # Eliminamos los caracteres que no sean alfanuméricos y convertimos el texto a minúsculas sin tildes

if sorted(texto1) == sorted(texto2): # Comparamos si los textos son anagramas
    print("Son anagramas --> Sí")
else:
    print("Son anagramas --> No")