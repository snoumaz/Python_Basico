"""
MATCJ = es switch de JS o JAVA
"""

mes = "Octubre"

match mes:
    case "Enero":
        print("Nos vamos a Japon")
    case "Febrero":
        print("Nos vamos a Paris")
    case "Marzo" | "Abril" | "Mayo":
        print("Nos vamos a Londres")
    case _:
        print("No se donde Ire")