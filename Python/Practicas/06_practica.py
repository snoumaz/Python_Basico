"""
ENTRADAS DEL CINE

Vamos a crear una app para vender entradas del cine.

Hay tres precios:
- Entrada estándar: 9.00
- Mayores de 65 años (seniors) : 6.90
- Infantiles : 7.20

Se puede vender cualquier cantidad de entradas,
pero los menores siempre deber ir acompañados
de un adulto.

Al finalizar la compra mostraremos las entradas 
y el importe total. 

En cualquier momento hay que poder finalizar 
el proceso sin que se produzca la compra

"""
import datetime
import os

# Variables globales


tarificacion = {"standar": 9.00 ,"senior":6.90,"child":7.20,"reduce":5.00}
#print(type(senior))
# tarifas = f"""¡¡Welcome a los Cines Ferran!!

# Tarifa de precios:

# Adultos {standar}
# Niños {child}
# Mayores {senior}

# Dia del espectador todos a {reduce}

# """
# print(tarifas)

menu = "Precios de las entradas"
for clase, valor in tarificacion.items():
        menu += f"\n{clase[0].upper()} {clase.capitalize()} : {valor:.2f} €"

        menu += "\n\nF. Finalizar la compra"
        menu += "\nX. Salir sin comprar"
        menu += "\n\nElija el tipo de entrada."
        menu += "\nA continuacion podra indicar la cantidad.\n>>>"

        eleccion_entrada = input(menu).lower().strip()
else:
    print("Opcion incorrecta.")
# adulto = input("¿Cuantos adultos son?\n")
# niño = input("¿Cuantos niños/as son?\n")
# mayores = input("¿Cuantos mayores a 65 son?\n")

def calculo () :
    if key in tarificacion:
        key = tarificacion.values(clave)
        resultado = float(adulto)*key
    return resultado
    
# def calculo_niño ():
#     if key in tarificacion:
#         key = tarificacion.values("child")
#         r_niños = float(niño)*key
#     return r_niños
                      
# def calculo_mayores () :
#     if key in tarificacion:
#         key = tarificacion.values("senior")
#         r_mayores = float(mayores)*key
#     return r_mayores

# # def espectador ():
#     if 

