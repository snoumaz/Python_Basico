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
#{}"ddjsdfnañksmjklans" .format(lkaskn)
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

numero_a = input("Introduce un Numero: ")
numero_b = input("Introduce un Numero: ")
operacion = input("Que operacion quieres")

if numero_a.isnumeric() or numero_b.isnumeric():
    pass
elif operacion == suma:
    print(f"{numero_a + numero_b}")
elif operacion == resta:
    print(f"{numero_a - numero_b}")
elif operacion == multi:
    print(f"{numero_a * numero_b}")
elif operacion == division:
    print(f"{numero_a / numero_b}")
elif operacion == divi_entera:
    print(f"{numero_a // numero_b}")
elif operacion == expo:
    print(f"{numero_a ** numero_b}")    
elif operacion == modulo:
    print(f"{numero_a % numero_b}")
else:
    print("No se puede hacer")

"""
Si numero_a, numero_b es numerico:
    formatea a enteros
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

 
