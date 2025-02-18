"""
Creacion clase
"""
class Animal():
    def __init__(self,especie):
        self.especie = especie
    def __str__(self):
        return f"La especie es {self.especie}"       

class Perro(Animal):
    def sonido(self):
        print("GUAUUUUUU!!!")

tortuga = Animal("Tortuga")

milu = Perro("Canido")
milu.sonido()
print(milu)

class Gato(Animal):
    def sonido(self):
        print("MIAUUUUUU!!!")

bola = Gato("Felino")
bola.sonido()

print(Perro.__base__)
print(Animal.__subclasses__())