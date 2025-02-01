# Importa el módulo os para operaciones del sistema
import os
# Limpia la pantalla de la consola
os.system("clear")

try:
    # Solicita y almacena el primer número, convirtiéndolo a decimal
    numero_a = float(input("Introduce un Numero: "))
    # Solicita y almacena el segundo número, convirtiéndolo a decimal
    numero_b = float(input("Introduce un Numero: "))
    # Muestra el menú de operaciones disponibles
    print("""
    Operaciones:
        suma
        resta
        multi
        division
        expo
        divi_entera
        modulo
    """)

    # Solicita al usuario que elija una operación
    op = input("¿Que operacion quieres realizar?")
    # Estructura match-case para evaluar la operación elegida
    match op: 
        # Si elige suma, realiza la adición de los números
        case "suma":
            print(f"{numero_a} + {numero_b} = {numero_a + numero_b}")
        # Si elige resta, realiza la sustracción
        case "resta":
            print(f"{numero_a} - {numero_b} = {numero_a - numero_b}")
        # Si elige multi, realiza la multiplicación
        case "multi":
            print(f"{numero_a} * {numero_b} = {numero_a * numero_b}")
        # Si elige division, realiza la división
        case "division":
            print(f"{numero_a} / {numero_b} = {numero_a / numero_b}")
        # Si elige divi_entera, realiza la división entera (sin decimales)
        case "divi_entera":
            print(f"{numero_a} // {numero_b} = {numero_a // numero_b}")
        # Si elige expo, realiza la potenciación
        case "expo":
            print(f"{numero_a} ** {numero_b} = {numero_a ** numero_b}")    
        # Si elige modulo, calcula el resto de la división
        case "modulo":
            print(f"{numero_a} % {numero_b} ={numero_a % numero_b}")
        # Caso por defecto si no coincide con ninguna operación anterior
        case _:
            print("Operacion no identificada")
# Maneja el error si el usuario no introduce un número válido
except ValueError:
    print("Introduce un numero en Cifras")
# Maneja el error si se intenta dividir entre cero
except ZeroDivisionError:
    print("No se puede dividir por Cero")

