import os
os.system("clear")

try:
    numero_a = float(input("Introduce un Numero: "))
    numero_b = float(input("Introduce un Numero: "))
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

    op = input("¿Que operacion quieres realizar?")
    match operacion: 
        case "suma":
            print(f"{numero_a} + {numero_b} = {numero_a + numero_b}")
        case "resta":
            print(f"{numero_a} - {numero_b} = {numero_a - numero_b}")
        case "multi":
            print(f"{numero_a} * {numero_b} = {numero_a * numero_b}")
        case "division":
            print(f"{numero_a} / {numero_b} = {numero_a / numero_b}")
        case "divi_entera":
            print(f"{numero_a} // {numero_b} = {numero_a // numero_b}")
        case "expo":
            print(f"{numero_a} ** {numero_b} = {numero_a ** numero_b}")    
        case "modulo":
            print(f"{numero_a} % {numero_b} ={numero_a % numero_b}")
        case _:
            print("Operacion no identificada")
except ValueError:
    print("Introduce un numero en Cifras")
except ZeroDivisionError:
    print("No se puede dividir por Cero")

