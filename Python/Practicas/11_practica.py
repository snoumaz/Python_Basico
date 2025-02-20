'''
Crea una clase llamada Vehiculo.

En su constructor incluye marca, modelo y año de construcción.

Dos métodos también:
-- arrancar, con el mensaje "El vehículo XX modelo YY ha arrancado"
-- detener, con el mensaje "El vehículo XX modelo YY se ha detenido"

Luego, dos clases hijas: Coche y Moto

La clase Coche tiene dos atributos propio: numero de puertas y AC (verdadero o falso).
y también un método propio: abrir_maletero, que
devuelve este mensaje: "El maletero del [marca] [modelo] está abierto"

La clase Moto tiene un método propio: revisar_seguridad, devuelve este mensaje:
"Si circulas en motocicleta debes llevar casco"
'''

class Vehiculo():
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def arrancar(self):
        return f"El vehiculo {self.marca} modelo {self.modelo} ha arrancado"
    def detener(self):
        return f"El vehiculo {self.marca} modelo {self.modelo} se ha detenido"
    
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año,puertas,ac):
        super().__init__(marca, modelo, año)
        self.puertas = puertas
        self.ac = ac
    def abrir_maletero(self):
        if self.puertas >=1:
            return f"El maletero del {self.marca} {self.modelo} está abierto"

class Moto(Vehiculo):
    # def __init__(self, marca, modelo, año):
    #     super().__init__(marca, modelo, año)

    def revisar_seguridad(self):
        return f"Si circulas en motocicleta debes llevar casco"    

coche_1 = Coche("Opel","Corsa",1992,3,"si")
moto_1 = Moto("Yamaha","MT09","2025")

print(coche_1.arrancar())
print(coche_1.detener())
print(coche_1.abrir_maletero())   

print(moto_1.arrancar())
print(moto_1.detener())
print(moto_1.revisar_seguridad())
