"""
Programación Orientada a Objetos: Biblioteca

El programa debe crear las siguientes clases con sus métodos:

    Clase Lector, que se construirá con nombre y apellido

    Clase Libro, que se construirá con nombre_autor, apellido_autor,
    y título

    Clase Biblioteca, que se construirá con nombre y dirección
    Esta clase dispondrá de los siguientes métodos:
    - agregar_lector: agrega un lector a la biblioteca
    - mostrar lectores
    - agregar_libro: agrega un libro a la biblioteca,
        indicando los ejemplare disponibles
    - buscar_libro: busca un libro en la biblioteca, 
        indicando si lo tiene o no
    - mostrar libros de la biblioteca

"""

# Creación de la clase Lector
class Lector:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.reservas = []  # Lista de libros reservados

    def __str__(self):
        return f"{self.nombre} {self.apellido} (Reservas: {len(self.reservas)})"

# Creación de la clase Libro
class Libro:
    def __init__(self, nombre_autor, apellido_autor, titulo, stock=1):
        self.nombre_autor = nombre_autor
        self.apellido_autor = apellido_autor
        self.titulo = titulo
        self.stock = stock  # Número de ejemplares disponibles
        self.lista_espera = []  # Lista de lectores esperando el libro

    def __str__(self):
        return f"'{self.titulo}' de {self.nombre_autor} {self.apellido_autor} (Stock: {self.stock})"

# Creación de la clase Biblioteca
class Biblioteca:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.lectores = []
        self.libros = []

    def agregar_lector(self, nombre, apellido):
        for lector in self.lectores:
            if lector.nombre == nombre and lector.apellido == apellido:
                return f"❌ El lector {nombre} {apellido} ya está registrado."

        nuevo_lector = Lector(nombre, apellido)
        self.lectores.append(nuevo_lector)
        return f"✅ Lector {nombre} {apellido} agregado con éxito."

    def agregar_libro(self, nombre_autor, apellido_autor, titulo, stock=1):
        for libro in self.libros:
            if libro.nombre_autor == nombre_autor and libro.apellido_autor == apellido_autor and libro.titulo == titulo:
                libro.stock += stock
                return f"📚 Se han añadido {stock} ejemplares del libro '{titulo}' de {nombre_autor} {apellido_autor}."

        nuevo_libro = Libro(nombre_autor, apellido_autor, titulo, stock)
        self.libros.append(nuevo_libro)
        return f"✅ Libro '{titulo}' de {nombre_autor} {apellido_autor} agregado con {stock} ejemplares."

    def busca_libro(self, nombre_autor, apellido_autor, titulo):
        for libro in self.libros:
            if libro.nombre_autor == nombre_autor and libro.apellido_autor == apellido_autor and libro.titulo == titulo:
                return f"🔍 El libro '{titulo}' de {nombre_autor} {apellido_autor} está disponible con {libro.stock} ejemplares."
        return f"❌ El libro '{titulo}' de {nombre_autor} {apellido_autor} no está en la biblioteca."

    def mostrar_libros(self):
        if not self.libros:
            return "📖 La biblioteca no tiene libros registrados."
        return "\n".join(str(libro) for libro in self.libros)

    def mostrar_lectores(self):
        if not self.lectores:
            return "👤 No hay lectores registrados."
        return "\n".join(str(lector) for lector in self.lectores)

    def reservar_libro(self, nombre_lector, apellido_lector, nombre_autor, apellido_autor, titulo):
        lector = next((l for l in self.lectores if l.nombre == nombre_lector and l.apellido == apellido_lector), None)
        libro = next((b for b in self.libros if b.nombre_autor == nombre_autor and b.apellido_autor == apellido_autor and b.titulo == titulo), None)

        if not lector:
            return f"❌ El lector {nombre_lector} {apellido_lector} no está registrado en la biblioteca."
        if not libro:
            return f"❌ El libro '{titulo}' de {nombre_autor} {apellido_autor} no está disponible en la biblioteca."

        if libro.stock > 0:
            libro.stock -= 1
            lector.reservas.append(libro)
            return f"✅ Reserva exitosa: {nombre_lector} {apellido_lector} ha reservado '{titulo}' de {nombre_autor} {apellido_autor}."
        else:
            libro.lista_espera.append(lector)
            return f"📌 No hay stock disponible. {nombre_lector} {apellido_lector} ha sido agregado a la lista de espera para '{titulo}'."

    def devolver_libro(self, nombre_lector, apellido_lector, titulo):
        lector = next((l for l in self.lectores if l.nombre == nombre_lector and l.apellido == apellido_lector), None)
        
        if not lector:
            return f"❌ El lector {nombre_lector} {apellido_lector} no está registrado en la biblioteca."

        libro_reservado = next((b for b in lector.reservas if b.titulo == titulo), None)
        
        if not libro_reservado:
            return f"❌ El lector {nombre_lector} {apellido_lector} no tiene reservado el libro '{titulo}'."

        lector.reservas.remove(libro_reservado)
        libro_reservado.stock += 1

        # Verificar si hay alguien en la lista de espera
        if libro_reservado.lista_espera:
            siguiente_lector = libro_reservado.lista_espera.pop(0)
            siguiente_lector.reservas.append(libro_reservado)
            libro_reservado.stock -= 1
            return f"🔄 {nombre_lector} {apellido_lector} ha devuelto '{titulo}', y ahora {siguiente_lector.nombre} {siguiente_lector.apellido} lo tiene reservado."
        
        return f"✅ {nombre_lector} {apellido_lector} ha devuelto '{titulo}'. El libro ahora está disponible."

# Creación de la biblioteca
biblioteca = Biblioteca("Biblioteca Nacional", "Calle Mayor, 10")

print(f"🏛️ La Biblioteca '{biblioteca.nombre}' está ubicada en {biblioteca.direccion}")

# Agregar lectores a la biblioteca
print(biblioteca.agregar_lector("Juan", "Perez"))
print(biblioteca.agregar_lector("Ana", "Gonzalez"))
print(biblioteca.agregar_lector("Carlos", "Gomez"))

# Agregar libros a la biblioteca
print(biblioteca.agregar_libro("Miguel", "de Cervantes", "Don Quijote", 5))
print(biblioteca.agregar_libro("Miguel", "de Cervantes", "El Quijote", 1))
print(biblioteca.agregar_libro("Durazno", "de Cervantes", "Don Quijote", 2))
# Reservar libros
print(biblioteca.reservar_libro("Juan", "Perez", "Miguel", "de Cervantes", "Don Quijote"))
print(biblioteca.reservar_libro("Ana", "Gonzalez", "Miguel", "de Cervantes", "Don Quijote"))  # Sin stock, va a lista de espera

# Devolver un libro
print(biblioteca.devolver_libro("Juan", "Perez", "Don Quijote"))  # Se libera y pasa a Ana

# Mostrar libros y lectores
print("\n📚 Lista de libros en la biblioteca:")
print(biblioteca.mostrar_libros())

print("\n👥 Lista de lectores en la biblioteca:")
print(biblioteca.mostrar_lectores())
