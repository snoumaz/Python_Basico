"""
LISTAS
"""

# Las listas equivalen a los  "Arrays" de otros leguajes
# Las lista se indican mediante corchetes -> []
# Las listas y los strings son "iterables" -> se pueden recorrer
# la separacion de elementos se realizan mediante comas
# la lista es una coleccion (de datos) indexada
# el indice empieza a contar en 0 

verdadero = True
lista = [1, 2, 3, 4, 5]
lista_nombres = ["Maria", "Pau", "Pol"] # lista de strings
lista_mixta = [1, "Maria", 3.5, True] # lista mixta
lista_de_lista = [[1, 2],["Pol", "Pau"], [True, verdadero]]

# Acceder al primer valor:
print(lista[0]) # 1
# Acceder al ultimo valor:
print(lista[-1]) # 5

# Slicing (el ultimo valor no esta incluido)
print(lista[1:3]) # [2, 3]
print(lista[-3:-1]) # [3, 4]

