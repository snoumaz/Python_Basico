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

print("Conversor de segundos\n")

try:
    segundos = int(input("Dime una cantidad de segundos a convertir: \n"))

    # Definición de unidades de tiempo en segundos
    segundos_minuto = 60
    segundos_hora = segundos_minuto * 60
    segundos_dia = segundos_hora * 24
    segundos_semana = segundos_dia * 7
    segundos_mes = segundos_dia * 30.44  
    segundos_año = segundos_dia * 365.25

    # Conversión de segundos a semanas, días, horas, minutos y segundos restantes
    años = segundos // segundos_año
    segundos %= segundos_año

    meses = segundos // segundos_mes
    segundos %= segundos_mes

    semanas = segundos // segundos_semana
    segundos %= segundos_semana

    dias = segundos // segundos_dia
    segundos %= segundos_dia

    horas = segundos // segundos_hora
    segundos %= segundos_hora

    minutos = segundos // segundos_minuto
    segundos %= segundos_minuto

    # Construcción del mensaje de salida
    resultado = str(segundos) + " segundos son "

    if años > 0:
        resultado += str(años) + " año" + ("s" if años > 1 else "") + ", "
    if meses > 0:
        resultado += str(meses) + " mes" + ("es" if meses > 1 else "") + ", "
    if semanas > 0:
        resultado += str(semanas) + " semana" + ("s" if semanas > 1 else "") + ", "
    if dias > 0:
        resultado += str(dias) + " día" + ("s" if dias > 1 else "") + ", "
    if horas > 0:
        resultado += str(horas) + " hora" + ("s" if horas > 1 else "") + ", "
    if minutos > 0:
        resultado += str(minutos) + " minuto" + ("s" if minutos > 1 else "") + " y "

    resultado += str(segundos) + " segundo" + ("s" if segundos != 1 else "")

    print(resultado)

except ValueError:
    print("Solo son válidos números.")
