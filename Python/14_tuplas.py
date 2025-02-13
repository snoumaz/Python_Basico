"""
TUPLAS
Es una colección INMUTABLE de datos
"""
mi_tupla = 3,4,5
print(type(mi_tupla))


tupla = ("Anna", "Pou", 20, "anna@email.com")
print(tupla)
# tupla[0] = "Marta"
lista_temporal = list(tupla)
print(lista_temporal)
lista_temporal[0] = "Marta"
print(lista_temporal)
tupla = tuple(lista_temporal)
print(tupla[1:3])

for elemento in tupla:
    print(elemento)
    