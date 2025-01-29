"""
 Caracteristicas basicas de Python
"""
"""
VARIABLES
Una variable es un espacio de memoria para guardar datos
por tanto, es un ConnectionAbortedError

Para crear una variable es necesario ..
identificador = valor

Hay reglas para llamar a los identificadores = de la variable
no se puede hacer:
1variable (empezar por numero, despues si lo puede llevar)
$variable (ni empezar ni contener simbolos especiales)
de estos errores nos avisa VSC

No de debemos hacer (no son exactamente errores):
    contener caracteres fuera del idioma ingles, como ñ, ç, tildes, Etc
    Empezar por guion bajo (reservado para determinadas situaciones)
    No debemos utilizar palabras utilizadas por el sistema  

Que debemos hacer:
    Nombra a nuestras variables con palabras descriptivas
    Podemos usar mas de una palabra separadas por un guion bajo (Directiva PEP-8)
    Intentar que las lineas de codigo no sean mu largas

Las variables tienen tipos:
    -- numeros => enteros (int), decimales (float), complejos ()
    -- texto => strings
    -- booleanos => True / False

Python es de tipado dinamico

numero = 1 # entero
numero = "uno" # string

Python es de tipado fuerte 

suma = numero + 2 # Error > no se pueden sumar numeros y texto
concatenacion = numero + str(2)
suma_numerica = int("1") + 2

En python, por defecto NO exiten las constante

PI = 3.1416

"""