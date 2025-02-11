"""
Ejercicio Diccionario

Tenemos un sitio que registra los accesos de los usuarios.
Necesitamos un menu con estas opciones:
1. Añadir un Usuario 
    (si no exite)
2. Añadir una visita al usuario indicado 
    ( si el usuario no exite mostar error)
3. Mostrar las visitas del usuario que se decida
    (si el usuario no exite mostar error)
4. Mostrar las visitas de todos los usuarios
    (si no hay usuarios todavia indicarlo)
X. para Salir

Hay que hacerlo con un diccionaro
"""

# Diccionario para almacenar los usuarios y sus visitas.
# La clave es el nombre del usuario y el valor es una lista con sus visitas.
usuarios = {}

while True:
    # Mostrar el menú
    print("\nMenú:")
    print("1. Añadir un Usuario")
    print("2. Añadir una visita al usuario indicado")
    print("3. Mostrar las visitas del usuario que se decida")
    print("4. Mostrar las visitas de todos los usuarios")
    print("X. Para Salir")

    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        case "1":
            # Añadir un Usuario (si no existe)
            nombre = input("Ingrese el nombre del usuario: ").strip()
            if nombre in usuarios:
                print("El usuario ya existe.")
            else:
                usuarios[nombre] = []  # Se inicializa con una lista vacía de visitas.
                print("Usuario agregado.")

        case "2":
            # Añadir una visita al usuario indicado (si el usuario no existe mostrar error)
            nombre = input("Ingrese el nombre del usuario: ").strip()
            if nombre not in usuarios:
                print("Error: El usuario no existe.")
            else:
                # Se añade una visita. Por ejemplo, se puede almacenar como "Visita 1", "Visita 2", etc.
                visita_numero = len(usuarios[nombre]) + 1
                usuarios[nombre].append("Visita " + str(visita_numero))
                print("Visita agregada para el usuario:", nombre)

        case "3":
            # Mostrar las visitas del usuario seleccionado (si el usuario no existe mostrar error)
            nombre = input("Ingrese el nombre del usuario: ").strip()
            if nombre not in usuarios:
                print("Error: El usuario no existe.")
            else:
                print("Visitas de", nombre + ":")
                if len(usuarios[nombre]) == 0:
                    print("  No hay visitas registradas.")
                else:
                    for visita in usuarios[nombre]:
                        print(" ", visita)

        case "4":
            # Mostrar las visitas de todos los usuarios (si no hay usuarios, indicarlo)
            if len(usuarios) == 0:
                print("No hay usuarios todavía.")
            else:
                for usuario in usuarios:
                    print("Usuario:", usuario)
                    if len(usuarios[usuario]) == 0:
                        print("  No hay visitas registradas.")
                    else:
                        for visita in usuarios[usuario]:
                            print(" ", visita)

        case "X" | "x":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")
