# Solucion 3 calculadora Ferran
import os
os.system("clear")
"""
try:
    respuesta = input("Inndica los numero y la operacion a realizar:\nEjemplo: 10, 5, +\n\n").split(", ")
    num_1 = float(respuesta[0])
    num_2 = float(respuesta[1])
    op = respuesta[2]

    match op:
        case "+" | "-" | "*" | "**" | "/" | "//" | "%":
            resultado = eval(f"{num_1} {op} {num_2}")
            print(f"{num_1} {op} {num_2} = {resultado}")  
        case _:
            print("Operacion desconocida")
            
except ValueError:
    print("Introduce un numero en Cifras")
except ZeroDivisionError:
    print("No se puede dividir por Cero")
"""
# Ejecicio Palindrono
# Solicitat al usuario un texto y le vas a decir si es un palindromo o no

texto1 = input("Escribe una frase: \n").strip() # Quita los espacios de delante y detras
print(texto1) # Muestra en pantalla 
texto2 = texto1.split(" ") # transforma en lista el texto usando los espacios en blanco como guia
print(texto2) # Muestra en pantalla
#texto3 = texto2.sorted(reverse=True) # coge la lista y la invierte .sort() es organizar y (reverse=True) lo invierte
#print(texto3)
