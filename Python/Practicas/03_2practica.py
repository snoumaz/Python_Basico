# Solucion 3 calculadora Ferran
import os
os.system("cls")
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
# Transforma en lista el texto usando los espacios en blanco como guia
palabras = texto1.split(" ") # Quita los espacios de la frase 
# Comprueba si la lista es palindroma
if palabras == palabras[::-1]: # Compara la lista con su inversa 
    print("La frase es palindroma")
else:  # Si no es palindroma, muestra el mensaje 
    print("La frase no es palindroma")


# Preguntale al usuario un mumero y dile si es par o inpar
num=input("Dime un numero: ") # Solicita un numero al usuario
if not num.isdigit():  # Comprueba que no se ha introducido un numero entero
    print("No has introducido un numero")
elif int(num) % 2 == 0: # Comprueba si el numero es par
    print(f"{num} es par") # Muestra el mensaje 
else: # Si no es par, muestra el mensaje 
    print(f"{num} es impar") #