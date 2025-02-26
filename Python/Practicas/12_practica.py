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
# Creacion clase lector
class Lector():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# Creacion Clase Libro
class Libro():
    def __init__(self, nombre_autor,apellido_autor, titulo,stock):
        self.nombre_autor = nombre_autor
        self.apellido_autor = apellido_autor
        self.titulo = titulo
        self.stock = stock  # Número de ejemplares disponibles
        self.lista_espera = []  # Lista de lectores esperando el libro

    def __str__(self):
        return f"'{self.titulo}' de {self.nombre_autor} {self.apellido_autor} (Stock: {self.stock})"


class Biblioteca():
    
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.lectores = []
        self.libros = []
        

    def agregar_lector(self, nombre, apellido):

        for lector in self.lectores: # Para el objeto lector en la lista lectores 
            if lector.nombre == nombre and lector.apellido == apellido: # Si el nombre y el apellido estan 
                return "Lector ya existe" # informa de que el lector esta

        # Si no existe, se agrega
        nuevo_lector = Lector(nombre, apellido) # Crea un nuevo objeto con los datos
        self.lectores.append(nuevo_lector) # añade a la lista lectores el nuevo lector
        return "Lector agregado con éxito" # Muestra en pantalla el mensaje

    def agregar_libro(self,nombre_autor,apellido_autor,titulo,stock=1):

        for libro in self.libros:
            if libro.nombre_autor == nombre_autor and libro.apellido_autor == apellido_autor and libro.titulo == titulo:
                libro.stock += stock
                return f"Se han añadido {stock} ejemplares del libro '{titulo}' de {nombre_autor} {apellido_autor}."

        nuevo_libro = Libro(nombre_autor, apellido_autor, titulo, stock)
        self.libros.append(nuevo_libro)
        return f"Libro '{titulo}' de {nombre_autor} {apellido_autor} agregado con {stock} ejemplares."


    def busca_libro(self, nombre_autor, apellido_autor, titulo):
        for libro in self.libros:
            if libro.nombre_autor == nombre_autor and libro.apellido_autor == apellido_autor and libro.titulo == titulo:
                return f"El libro '{titulo}' de {nombre_autor} {apellido_autor} está disponible con {libro.stock} ejemplares."
        return f"El libro '{titulo}' de {nombre_autor} {apellido_autor} no está en la biblioteca."

    def mostrar_libros(self):
        if not self.libros:
            return "La biblioteca no tiene libros registrados."
        return "\n".join(str(libro) for libro in self.libros)


# Creación de la biblioteca
biblioteca = Biblioteca("Biblioteca Nacional", "Calle Mayor, 10")

print(f"La Biblioteca {biblioteca.nombre}, está ubicada en {biblioteca.direccion}")

# Agregar lectores a la biblioteca
print(biblioteca.agregar_lector("Juan", "Perez"))
print(biblioteca.agregar_lector("Ana", "Gonzalez"))
print(biblioteca.agregar_lector("Juan", "Perez")) 
print(biblioteca.agregar_lector("Juan", "Gonzalez")) # Intento agregar un lector que ya existe

# Agregar libros a la biblioteca
print(biblioteca.agregar_libro("Miguel","de Cervantes","Don Quijote"))
print(biblioteca.agregar_libro("Miguel","de Cervantes","El Quijote"))
print(biblioteca.agregar_libro("Miguel","de Cervantes","Don Quijote"))
print(biblioteca.agregar_libro("Miguel","Lara","Don Quijote"))
print(biblioteca.agregar_libro("Rafa","de Cervantes","Yo y yo"))


print("\nLista de libros en la biblioteca:")
print(biblioteca.mostrar_libros())