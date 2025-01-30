# Pedir al usuario un numero
numero_a = input("Introduce un número: ")
numero_b = input("Introduce otro número: ")
operacion = input("""¿Qué operación quieres realizar?
1. suma
2. resta
3. multi
4. division
5. expo
6. divi_entera
7. modulo
Tu elección: """)

# Verificar si los números son válidos (enteros, decimales o negativos)
def es_numero_valido(num):
    # Eliminar el signo negativo si existe
    if num.startswith('-'):
        num = num[1:]
    # Verificar si es entero o decimal
    return num.isnumeric() or (num.replace(".", "", 1).isdecimal() and num.count(".") == 1)

if es_numero_valido(numero_a) and es_numero_valido(numero_b):
    # Convertir a float
    num_a = float(numero_a)
    num_b = float(numero_b)
    
    # Verificar la operación
    if operacion == "suma":
        print(f"{num_a} + {num_b} = {num_a + num_b}")
    elif operacion == "resta":
        print(f"{num_a} - {num_b} = {num_a - num_b}")
    elif operacion == "multi":
        print(f"{num_a} * {num_b} = {num_a * num_b}")
    elif operacion == "division":
        if num_b == 0:
            print("No se puede dividir por cero")
        else:
            print(f"{num_a} / {num_b} = {num_a / num_b}")
    elif operacion == "expo":
        print(f"{num_a} ** {num_b} = {num_a ** num_b}")
    elif operacion == "divi_entera":
        if num_b == 0:
            print("No se puede dividir por cero")
        else:
            print(f"{num_a} // {num_b} = {num_a // num_b}")
    elif operacion == "modulo":
        if num_b == 0:
            print("No se puede dividir por cero")
        else:
            print(f"{num_a} % {num_b} = {num_a % num_b}")
    else:
        print("Operación no válida")
else:
    print("Por favor, introduce números válidos")