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

# Creacion Clase 
class Libro():
    """
    Definiendo el contructor con los atributos:\n
    - Autor: Nombre y Apellidos\n
    - Titulo: Titulo del libro\n
    - Cantidad: Atributo oculto\n
    """
    def __init__(self, autor, titulo):
        self.autor = autor
        self.titulo = titulo
        self.cantidad = 0

    def __str__(self):
        return f"Libro {self.titulo} del autor {self.autor}"

# Creacion Clase 
class Lector():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"Lector: {self.nombre} {self.apellido}"

# Creacion Clase 
class Biblioteca():
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_libros = []
        self.lista_lectores = []
        self.diccio_reservas = {}
    def __str__(self):
        return f"Bienvenido a la Biblioteca {self.nombre}, ubicada en {self.direccion}"