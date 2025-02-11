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


# lista_dics = [{"usuario":"Anton"},{"usuario":"Pepe"},{"usuario":"Maria"}]
# try:
#     print("""Menu \n1. Añadir un Usuario\n2. Añadir una visita al usuario indicado
# 3. Mostrar las visitas del usuario que se decida\n4. Mostrar las visitas de todos los usuarios\nX. para Salir""")
#     opciones = input("Elige: \n").lower
    
#     #print(usuario)

#     while "x" in opciones:
#         usuario = input("Que usuario buscas: \n").lower().capitalize()
#         match opciones:
#             case "1":
#                 lista_dics.get("usuario":f"{usuario}","visita":f"{visita +=1}")
#             case "2":
#                 lista_dics.append(visita +=1 "Al usuario")
#             case "3":
#                 if usuario != lista_dics.__getattribute__(usuario):
#                     print("El usuario no exite")
        
# except:
#     print("Error")


# FERRAN Solucion
#import os
#os.system("cls")
users = []
while True:
    menu = """
1. Añadiremos un usuario 
2. Añadiremos una visita al usuario indicado 
3. Mostraremos las visitas del usuario que se decida
4. Mostraremos las visitas de todos los usuarios
X. Salir
"""
    print(menu)
    opcion = input("Elige tu opcion --> ").strip().lower()

    match opcion:
        case "1":
            new_user = input("Nuevo usuario --> ").strip().title()
            
            if users:
                user_in_list = 0
                for user in users:
                    if user['nombre'] != new_user:
                        user_dic = {"nombre":new_user, "visitas": 0 }
                        users.append(user_dic)
                        print(f"Usuario {new_user} añadido")
                        break
                    else:
                        print("El usuario ya existe")
        case "2":       
            # if users:
            #     user = input("Usuario --> ").strip().title()
            #     for user in users:
            #         if user['nombre'] == user:
            #             user['visitas'] += 1
            #             print("Visita añadida")
            #         else:
            #             print("El usuario no existe")
            # else:
            #     print("No hay usuarios todavía")
            pass
        case "3":
            # if users:
            #     user = input("Usuario --> ").strip().title()
            #     for user in users:
            #         if user['nombre'] == user:
            #             print(f"El usuario {user['nombre']} ha tenido {user['visitas']} visitas")
            #         else:
            #             print("El usuario no existe")
            # else:
            #     print("No hay usuarios todavía")
            pass
        case "4":
            if users:
                print(users)
            else:
                print("No hay usuarios todavía")
        case "x":
            print("Fin del programa")
            break
        case _ :
            print("Opción no reconocida.\nVuélvelo a probar.")

print(users)