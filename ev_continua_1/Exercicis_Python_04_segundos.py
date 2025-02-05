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

segundos_ingresados = int(input("Conversor de segundos\nIngrese la cantidad de segundos: "))

semanas = segundos_ingresados // 604800
segundos_ingresados %= 604800
dias = segundos_ingresados // 86400
segundos_ingresados %= 86400
horas = segundos_ingresados // 3600
segundos_ingresados %= 3600
minutos = segundos_ingresados // 60
segundos_ingresados %= 60

resultado = []
if semanas > 0:
    resultado.append(f"{semanas} semana{'s' if semanas > 1 else ''}")
if dias > 0:
    resultado.append(f"{dias} día{'s' if dias > 1 else ''}")
if horas > 0:
    resultado.append(f"{horas} hora{'s' if horas > 1 else ''}")
if minutos > 0:
    resultado.append(f"{minutos} minuto{'s' if minutos > 1 else ''}")
if segundos_ingresados > 0 or not resultado:
    resultado.append(f"{segundos_ingresados} segundo{'s' if segundos_ingresados > 1 else ''}")

print(f"{segundos_ingresados} segundos son " + " y ".join(resultado) + ".")
