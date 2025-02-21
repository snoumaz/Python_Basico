class Restaurante():
    # Creacion del constructor
    def __init__(self, nombre, especialidad, turnos):
        self.nombre = nombre
        self.especialidad = especialidad
        self.turnos = turnos
        self.dic_reserva = {turno: [] for turno in turnos}

    def reserva(self, cliente, turno_r):
        if turno_r in self.turnos:
            if len(self.dic_reserva[turno_r]) < 3:
                self.dic_reserva[turno_r].append(cliente.nombre)
                print(f"Reserva realizada por {cliente.nombre} en el turno {turno_r}.")
            else:
                print(f"No se ha podido realizar la reserva. Pruebe en otro turno.")
        else:
            print(f"Turno {turno_r} no disponible.")

class Cliente():
    # Creacion del constructor
    def __init__(self, nombre):
        self.nombre = nombre

# Ejemplo de uso
restaurante_1 = Restaurante("Can Pizza", "Cocina Italiana", (13, 14, 15, 20, 21, 22))
cliente_1 = Cliente("Anna")

# Realizar una reserva
restaurante_1.reserva(cliente_1, 13)
restaurante_1.reserva(cliente_1, 13)
restaurante_1.reserva(cliente_1, 55)
restaurante_1.reserva(cliente_1, 13)  # Intentar reservar en un turno ya lleno


print(restaurante_1.dic_reserva)