"""
Bucles
"""

# for -> para elementos controlados

nombres = ["Juan", "Maria", "Pol", "Pau"]
edades = [25, 30, 45, 80, 90]
"""
# para cada nombre que este en la lista nombre ...
for nombre in nombres:
    print(nombre)
"""  
    
# impirmir pantalla p
"""
for nombre in nombres:
    nombre = nombre.startswith("P")
    if nombre is True:
        print(str(nombre))
    print(type(nombre))
"""
"""
# Solucion Ferran
check = input("Porque letra empieza el nombre de quien buscas? \n")
# crear el bucle para acceder a cada elemento de la lista
for nombre in nombres:
    #if nombre[0].lower() == check.lower():
    #     print(nombre.capitalize())      
    if nombre.lower().capitalize(check.lower()):
        print(nombre.capitalize())
"""
# while = mientras -> para elementos no controlados
"""
num = 5
while num > 0: # Hasta que la variable no llega a 0 el bucle continua
    print(num)
    num -= 1
else:
    print("Estas en el else")
print("#"*20)
while True:
    print(num)
    num -= 1
    if num == 0:
        break
else:
    print("Estas en el else")
"""
monedas = float(input("cuantas monedas tengo? \n"))
while True:
    prestamo = float(input("¿Cuantas monedas necesitas? \n"))
    if prestamo <= monedas:
        monedas -= prestamo
    elif prestamo > monedas > 0:
        print("No hay suficiente")
    else:
        print("No hay cash")
        break

    
