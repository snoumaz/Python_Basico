"""
Crear un programa que utilice un diccionaro para almacenar de un inventario de productos.
Hay que guardar 5 productos con sus cantidades.
Despues añadiremos dos nuevos productos.
Actualizaremos las cantidades de 2 productos cualquiera.
Mostrar ahora todos los productors y sus cantidades.
"""

inventario = {"tomates": 10,"platanos":5,"peras":9,"manzanas":4,"sandias":2}

contador = 1
while contador <= repeticiones:
    repeticiones = 0
    menu = f"""
    Opciones:
    \t 1.- Añadir a la lista de productos
    \t 2.- Mostrar la lista de productos
    \t 3.- Salir
    """
    opcion_user = input("Que opcion eliges ==> ").strip()
    
    if opcion_user not in ["1","2","3"]:
        print("Introduce una de las 3 opciones")
    
