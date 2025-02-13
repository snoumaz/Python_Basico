"""
FUNCIONES
"""

# Declaración 1
def sumar () :
    print(1 + 2)

# Invocación
sumar()

# Declaración 2
def sumar () :
    return 1 + 2

print(sumar())

# Declaración 3
# En la declaración lo que hay en 
# los paréntesis son los PARÁMETROS
def sumar (num1, num2) :
    return num1 + num2

# En la ejeccución/invocación lo que hay en 
# los paréntesis son los ARGUMENTOS
print(sumar(3, 7))
print(sumar(3.5, 7.2))
print(sumar("Hola ", "y adiós"))

resultado = sumar(2, 3)

# Ejemplos de funciones:
# -- para ver si un número es primo o no
# -- para corregir nombres mal escritos
# -- para calcular días, horas, etc de una contidad de segundos
# -- para calcular los días que faltan para una fecha

variable = "Otra cosa"

def prueba_variable() :
    variable = "Soy una prueba"
print(variable)

def mostrar_datos_alumno(nombre, apellido, becado = False):
    if becado:
        becado = "Sí"
    else:
        becado = "No"
    return f"¿el alumno {nombre} {apellido} tiene beca? --> {becado}"
    
alumno_1 = mostrar_datos_alumno("Anna", "Garcia")
print(alumno_1)
alumno_2 = mostrar_datos_alumno("Joan", "Pou", True)
print(alumno_2)

def sumar(*argv) :
    print(type(argv))

sumar(1,2)
sumar(3,4,5)
sumar(3,7,907)