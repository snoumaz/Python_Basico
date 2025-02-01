# Pedir al usuario un numero
# Pedir otro numero
# Si no son numeros, le diremos que no se puede hacer 
# Pedir que operacion quiere hacer (7 posibilades)
    # Suma
    # resta
    # multi
    # division
    # expo
    # divi_entera
    # modulo
# Si no es ninguna de estas un mensaje de error
# Si divide por 0 tambien error

import os # importa libreria OS 
os.system("clear") # Pide realizar el comando del sistema que ponemos entre parentesis 

try:
    numero_a = float(input("Introduce un Numero: ")) # Introduccion de datos que se transforman en decimales con la funcion float()
    numero_b = float(input("Introduce un Numero: ")) # Introduccion de datos que se transforman en decimales con la funcion float()


    operacion = input("""Que operacion quieres:  
    suma
    resta
    multi
    division
    expo
    divi_entera
    modulo
    Escribe la palabra de la operacion: \n\n""") # Variable donde se solicita una introducion de datos
    
    
    #suma = "suma"
    #resta = "resta"
    #multi = "multi"
    #division = "division"
    #expo = "expo"
    #divi_entera = "divi_entera"
    #modulo = "modulo"
    if operacion == "suma": # Comparacion de si la variable operacion es igual a suma realiza la operacion de abajo
        print(f"{numero_a} + {numero_b} = {numero_a + numero_b}") # (f"{}") -> Cambia el formato de lo que hay entre corchetes a numeros  manteniendo el resto en las comillas como strings
    elif operacion == "resta": # Comparacion de si la variable operacion es igual a resta realiza la operacion de abajo
        print(f"{numero_a} - {numero_b} = {numero_a - numero_b}") # (f"{}") -> Cambia el formato de lo que hay entre corchetes a numeros  manteniendo el resto en las comillas como strings
    elif operacion == "multi": # Comparacion de si la variable operacion es igual a multi realiza la operacion de abajo
        print(f"{numero_a} * {numero_b} = {numero_a * numero_b}") # (f"{}") -> Cambia el formato de lo que hay entre corchetes a numeros  manteniendo el resto en las comillas como strings
    elif operacion == "division": # Comparacion de si la variable operacion es igual a division realiza la operacion de abajo
        print(f"{numero_a} / {numero_b} = {numero_a / numero_b}") # (f"{}") -> Cambia el formato de lo que hay entre corchetes a numeros  manteniendo el resto en las comillas como strings
    elif operacion == "divi_entera": # Comparacion de si la variable operacion es igual a division entera realiza la operacion de abajo
        print(f"{numero_a} // {numero_b} = {numero_a // numero_b}") # (f"{}") -> Cambia el formato de lo que hay entre corchetes a numeros  manteniendo el resto en las comillas como strings
    elif operacion == "expo": # Comparacion de si la variable operacion es igual a exponencial realiza la operacion de abajo
        print(f"{numero_a} ** {numero_b} = {numero_a ** numero_b}") # (f"{}") -> Cambia el formato de lo que hay entre corchetes a numeros  manteniendo el resto en las comillas como strings   
    elif operacion == "modulo": # Comparacion de si la variable operacion es igual a modulo realiza la operacion de abajo
        print(f"{numero_a} % {numero_b} ={numero_a % numero_b}") # (f"{}") -> Cambia el formato de lo que hay entre corchetes a numeros  manteniendo el resto en las comillas como strings
    else: # si no cumple con ninguno de los casos anteriores haz lo que pone
        print("No se puede hacer")
except ValueError: # ValueError indica que si el valor introducido por el usuario no es del tipo indicado de el siguiente mensaje
    print("Introduce un numero en Cifras")
except ZeroDivisionError: # ZeroDivisionError  indica que si el valor introducido por el usuario es 0 a la hora de dividir de el siguiente mensaje
    print("No se puede dividir por Cero")
finally:
    print("Resultado")
