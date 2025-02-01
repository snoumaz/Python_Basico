"""
MATCJ = es switch de JS o JAVA
"""

mes = "Octubre"

match mes: # Match permite comparar varias opciones
    case "Enero": # Caso cuando el mes es Enero muestra en pantalla que nos vamos a Japon
        print("Nos vamos a Japon")
    case "Febrero": # Caso cuando el mes es Febrero muestra en pantalla que nos vamos a Paris
        print("Nos vamos a Paris")
    case "Marzo" | "Abril" | "Mayo": # Caso cuando el mes es Marzo, Abril o Mayo muestra en pantalla que nos vamos a Londres
        print("Nos vamos a Londres")
    case _: # Caso por defecto muestra en pantalla que no se donde iremos
        print("No se donde Ire")