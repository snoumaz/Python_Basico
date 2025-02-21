"""
Vamos a gestionar restaurantes. (Objetos)
Cada uno tiene: (atributos)
-- Nombre
-- Especialidad
-- Turnos 
    -- Puede hacer como maximo 3 clientes por turnos
    -- Si se  realiza la reserva diremos " Reserva realizada por {cliente}"
    -- Y si no "No se ha podido realizar las reserva. pruebe en otro truno"
-- Clientes

Clientes vamos a necesitar ( de momento)
-- Nombre

ejemplo de uso:
cliente_1 = Cliente("Anna")
"""

# Creamos la Clase Cliente

class Cliente(): # Classe Cliente
    def __init__(self,name): # Definimos el constructor de la clase con el atributo name, el atributo self es para definir el resto
        self.name = name


# Creamos la clase Restaurante

class Restaurante(): # Classe Restaurante
    
    def __init__(self,name,type,turn): # Definimos el constructor de la clase con los atributos name, type y turn.  
        self.name = name
        self.type = type
        self.turn = turn
        self.diccionario_reservas= {} # Creamos el diccionario_reservas vacio, para luego rellenarlo, este dicccionario es un atributo oculto
        for hora in turn:  # Para el valor facilitado por tanto el usuario o si lo definimos lo compara con los datos en turn 
            self.diccionario_reservas[hora]=0 # Rellenamos el diccionario con la clave hora y el valor 0

    def reservas(self,client,hora): # Creamos el metodo con los atributos cliente y hora
        if hora not in self.turn: # si hora no esta en turno, para y printa
            return f"El horario {hora} no esta dentro de los horarios del restaurante."
        if self.diccionario_reservas[hora] < 3: # Si el valor de hora en el diccionaro es menor a 3 continua
            self.diccionario_reservas[hora] += 1 # Suma 1 al valor y muestra en pantalla el mensaje
            return f"Reserva realizada {client.name}"
        else:
            return "La reserva no se ha podido realizar, pruebe en otro horario." # En caso que no entre en ninguno de los casos muestra el mensaje
        

cliente_1 = Cliente("Anna") # Creamos el objeto cliente_1
restaurante_1 = Restaurante("Can Pizza","Cocina Italiana",(13,14,15,20,21,22))  # Creacion objeto restaurante_1    



print(restaurante_1.reservas(cliente_1, 14)) # muestra en pantalla la reserva