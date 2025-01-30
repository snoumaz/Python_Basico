# Preguntar edad Usuario
# si tiene menos de 12 años eres un/a niño/a
# si tienes menos de 18 años eres un adolescente
# si tienes menos de 30 años eres joven
# si tienes menos de 40 años eres adulto
# si tienes mas de 40 tu puedes con todo

edad = int(input("Pon tu edad ->"))

if 1 < edad < 12:
    print("Eres un niño/a")
elif edad <= 18:
    print("Eres adolescente")
elif edad <= 30:
    print("Eres Joven")
elif edad <= 40:
    print("Eres adulto")
else:
    print("Tu puedes con todo")