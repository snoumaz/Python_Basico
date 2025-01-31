# Preguntar edad Usuario
# si tiene menos de 12 años eres un/a niño/a
# si tienes menos de 18 años eres un adolescente
# si tienes menos de 30 años eres joven
# si tienes menos de 40 años eres adulto
# si tienes mas de 40 tu puedes con todo
"""
edad = int(input("Pon tu edad ->"))

if 0 <= edad < 12:
    print("Eres un niño/a")
elif edad <= 18:
    print("Eres adolescente")
elif edad <= 30:
    print("Eres Joven")
elif edad <= 40:
    print("Eres adulto")
elif edad <= 120:
    print("Tu puedes con todo")
else:
    print("Tienes 2 pies en la tumba")
"""
# Preguntar al usuario la edad
# si tiene 0 o mas de 120: No me lo creo
# si tiene menos de 18: Aun no puedes votar, te faltan x años
# si tienes mas de 18: Puedes votar desde hace x años
"""
edad = int(input("Pon tu edad ->"))

if 0 > edad:
    print('NO me lo creo')
elif edad < 18:
    print(f"Aun no puedes votar, te faltan {18 - edad} años")
elif edad >= 18:
    print("Puedes votar desde hace " + str(edad - 18) + " años")
elif edad >= 120:
    print("No me lo creo")
else:
    pass
"""
"""
# Solucion ferran

mayoria_edad = 18 # Variable determinar la mayoria edad

edad = input("Porfavor indica tu edad: ") # Variable donde el usuario introduce su edad en formato string utiluzando el comando input

if not edad.isdigit(): # Comprobacion que no se ha introducido un numero entero
    print("Debes introducir un numero entero") # Imprime en pantalla el mensaje entre comillas
elif 0 >= int(edad) >= 120: # Si la edad es menos o mas de 120 int = convierte el string a entero ==> comprobacion rango de edad valido
    print("No me lo creo") # Imprime en pantalla el mensaje entre comillas
else:
    edad = int(edad)  # Convierte string en entero
    diferencia = abs(mayoria_edad - edad) # variable que hace el valor absoluto de la mayoria de edad y la edad
    if edad <  mayoria_edad:
        print(f"Aun no puedes votar, te faltan {diferencia} años")
"""
"""
Si numero_a, numero_b es numerico:
    formatea a enteros
Si es decimal o no:
    formatear a decimales
Si numero_a y numero _b son negativos:
    tener en cuenta si son negativos
sino:
    muestra Eso no se puede hacer
solicita operacion:
    si es suma numero_a + numero_b = resuldado
elif 
    si es suma numero_a + numero_b = resuldado
elif
    si es suma numero_a + numero_b = resuldado
elif
    si es suma numero_a + numero_b = resuldado
elif
    si es suma numero_a + numero_b = resuldado
elif
    si es suma numero_a + numero_b = resuldado
elif
    si es suma numero_a + numero_b = resuldado
sino:
    Error
"""
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
"""
import os
os.system("clear")

try:
    numero_a = float(input("Introduce un Numero: "))
    numero_b = float(input("Introduce un Numero: "))


    operacion = input(#Que operacion quieres:
    #suma
    #resta
    #multi
    #division
    #expo
    #divi_entera
    #modulo
    #Escribe la palabra de la operacion:
    
    
    #suma = "suma"
    #resta = "resta"
    #multi = "multi"
    #division = "division"
    #expo = "expo"
    #divi_entera = "divi_entera"
    #modulo = "modulo"
    if operacion == "suma":
        print(f"{numero_a} + {numero_b} = {numero_a + numero_b}")
    elif operacion == "resta":
        print(f"{numero_a} - {numero_b} = {numero_a - numero_b}")
    elif operacion == "multi":
        print(f"{numero_a} * {numero_b} = {numero_a * numero_b}")
    elif operacion == "division":
        print(f"{numero_a} / {numero_b} = {numero_a / numero_b}")
    elif operacion == "divi_entera":
        print(f"{numero_a} // {numero_b} = {numero_a // numero_b}")
    elif operacion == "expo":
        print(f"{numero_a} ** {numero_b} = {numero_a ** numero_b}")    
    elif operacion == "modulo":
        print(f"{numero_a} % {numero_b} ={numero_a % numero_b}")
    else:
        print("No se puede hacer")
except ValueError:
    print("Introduce un numero en Cifras")
except ZeroDivisionError:
    print("No se puede dividir por Cero")
finally:
    print("Resultado")

"""
# Solulcion Ferran
"""
num_1 = input("Escriba el primer numero -> ")
# provar "1", "1.2", "uno", "??"
if num_1.isalpha(): # Comprobacion que el dato introducido es caracter o numerico isalpha incluye caracteres y simbolos = true
    print("No se puede hacer")
else:
    print("Se puede hacer")

# Excepciones
num_1 = float(input("Escriba el primer numero -> "))
# provar "1", "1.2", "uno", "??"
if num_1.isalpha(): # Comprobacion que el dato introducido es caracter o numerico isalpha incluye caracteres y simbolos = true
    print("No se puede hacer")
else:
    print("Se puede hacer")
"""
"""
# Se puede producir una excepcion a causa de lo que introduzca el usuario:
try:
    # Pedimos los numeros
    num_1 = float(input("Introduce un numero: "))
    num_2 = float(input("Introduce un numero: "))
    print("""
    #Operaciones:
    #   suma
    #    resta
    #    multi
    #   division
    #   expo
    #   divi_entera
    #   modulo
    
"""
    op = input("¿Que operacion quieres realizar?")

    if op == "suma":
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    elif op == "resta":
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    elif op == "multi":
        print(f"{num_1} * {num_2} = {num_1 * num_2}")
    elif op == "division":
        print(f"{num_1} / {num_2} = {num_1 / num_2}")
    elif op == "divi_entera":
        print(f"{num_1} // {num_2} = {num_1 // num_2}")
    elif op == "expo":
        print(f"{num_1} ** {num_2} = {num_1 ** num_2}")
    elif op == "modulo":
        print(f"{num_1} % {num_2} = {num_1 % num_2}")
except ValueError:
    print("Has de describir un numero en cifra")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
"""

# Calculadora a base de mathc

import os
os.system("clear")
"""
try:
    numero_a = float(input("Introduce un Numero: "))
    numero_b = float(input("Introduce un Numero: "))
    print"""("""
    Operaciones:
        suma
        resta
        multi
        division
        expo
        divi_entera
        modulo
    """)
"""
    op = input("¿Que operacion quieres realizar?")
    match operacion: 
        case "suma":
            print(f"{numero_a} + {numero_b} = {numero_a + numero_b}")
        case "resta":
            print(f"{numero_a} - {numero_b} = {numero_a - numero_b}")
        case "multi":
            print(f"{numero_a} * {numero_b} = {numero_a * numero_b}")
        case "division":
            print(f"{numero_a} / {numero_b} = {numero_a / numero_b}")
        case "divi_entera":
            print(f"{numero_a} // {numero_b} = {numero_a // numero_b}")
        case "expo":
            print(f"{numero_a} ** {numero_b} = {numero_a ** numero_b}")    
        case "modulo":
            print(f"{numero_a} % {numero_b} ={numero_a % numero_b}")
        case _:
            print("Operacion no identificada")
except ValueError:
    print("Introduce un numero en Cifras")
except ZeroDivisionError:
    print("No se puede dividir por Cero")
finally:
    return 0
"""
# Preguntar al usuario que dia de la se mana es:
# si dice lunes toca sistemas
# si dice martes miercoles jueves o viernes toca programacion
# si dice sabado domingo descansa coño
# si dice otra cosa Creo que estas confundido

dia = input("Que dia de la semana estamos: ")
dia = dia.lower()
match dia:
    case "lunes":
        print("Hoy toca sistemas.")
    case "martes" | "miercoles" | "jueves" | "viernes":
        print("Hoy toca Python.")
    case "sabado" | "domingo":
        print("Es fin de semana.")
    case _:
        print("Creo que estas confundido.")
return 0