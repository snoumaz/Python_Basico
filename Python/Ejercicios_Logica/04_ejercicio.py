"""
Tenemos esta lista de animales

Vamos a pedir una letra al usuario
Mostraremos los animales que continen esa letra
Y si no hay ninguno diremos "Ningun animal contiene esa letra"
"""
import os
os.system("cls")
animales = ["gato", "perro", "caballo", "paloma", "murcielago","leon", "mono"]

try:
    letra = input("Introduce una letra: \n").lower()
    if not letra.isalpha():
        print("Ha de ser una letra del abecedario")
    else:
        for animal in animales:
            busca = animal.find(letra)
            if busca == True:
                print(animal)         
    if busca != True:
        print("Ningun animal contiene esa letra")
except:
    pass    
    

    