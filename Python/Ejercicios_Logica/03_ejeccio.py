"""
Solicita al usuario un numero y haz la tabla de multiplicar 
"""
import os
os.system("cls")
try:
    numero = int(input("Introduce un numero del 1 al 10 \n"))
    if 0<= numero <= 10:
        for num in range(11):
            print(f"{numero} * {num} = {numero*num}")
    else:
        print("Solo numeros del 1 al 10")
except ValueError:
    print("Solo son validos numeros")

try:
    numero = int(input("Introduce un numero del 1 al 10 \n"))
    for num in range(11):
        print(f"{numero} * {num} = {numero*num}")
except ValueError:
    print("Solo son validos numeros")