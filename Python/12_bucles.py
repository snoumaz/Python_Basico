"""
Bucles
"""

# for -> para

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

# Solucion Ferran
check = input("Porque letra empieza el nombre de quien buscas? \n")
# crear el bucle para acceder a cada elemento de la lista
for nombre in nombres:
    #if nombre[0].lower() == check.lower():
    #     print(nombre.capitalize())      
    if nombre.lower().capitalize(check.lower()):
        print(nombre.capitalize())

