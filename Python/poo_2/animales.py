"""
Creacion clase
"""
class Animal():
    pass

class Perro(Animal):
    def sonido(self):
        print("GUAUUUUUU!!!")

milu = Perro()
milu.sonido()

class Gato(Animal):
    def sonido(self):
        print("MIAUUUUUU!!!")

bola = Gato()
bola.sonido()

print(Perro.__base__)
print(Animal.__subclasses__())