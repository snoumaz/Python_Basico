"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 4
Mostraremos el mensaje: "Conversor de segundos"
A continuación pediremos al usuario una cantidad de segundos.

Le responderemos:
- Si son menos de 60 segundos, mostrará "X segundos son menos de 1 minuto"
- Si es igual o superior a 60 segundos le diremos:
    "X segundos son Y minutos y Z segundos"

Y así para las siguientes unidades de tiempo. Por tanto, si la cantidad de segundos 
supera la hora, le diremos cuantas horas, minutos y segundos son. 
Lo mismo si supera un día o una semana. 

. 
"""
import os
os.system("cls")
secs = 60
mins = 60
horas = 24
dias = 7
mes = 4
año = 12 
print("Conversor de segundos\n")
try:
    segundos=int(input("Dime una cantidad de segundos a convertir: \n"))
    

except ValueError:
    print("Solo son validos numeros")