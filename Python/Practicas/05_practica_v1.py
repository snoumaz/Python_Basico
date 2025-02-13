"""
Juego de piedra papel tijera
"""
"""
Introducciones normas juegos
Menu de seleccion de las tres opciones 
El usuario introduce valores "piedra", "papel", "tijera"
el programa randomiza entre los 3 valores y los compara en cada caso.
en cada caso hay que mostras o as ganado o as perdido.
contadores de cuanto a ganado cada uno
"""
"""
LISTA DE MEJORAS
- Jugar mas de 1 una vez
- Limitar un maximo de partidas
- Contar cuantas veces a ganado, perdido o empatado cada 1
- Personalizar solicitando el nombre
- Poder guardar el resultados
- Procentaje de victorias
- 
"""

import random
# Lista opciones del juego
lista = ["Piedra","Papel","Tijeras"]
opciones_juego = ['🪨','⬜','✂️']
menu = f"""
PIERDRA - PAPEL - TIJERAS
=========================

Selecciona 1 de las 3 opciones para jugar:

1.- {lista[0]}{opciones_juego[0]}
2.- {lista[1]}{opciones_juego[1]}
3.- {lista[2]}{opciones_juego[2]}

En caso de no querer jugar o salir del juego pulsa qualquier tecla
fuera de las 3 opciones.

Buena suerte y pasalo bien.

"""

print(menu)


opcion_user = input("Que opcion eliges ==> ").strip()
if opcion_user not in ["1","2","3"]:
    print("El juego a finalizazo. ¡Hasta pronto!")
else:
    opcion_pc = str(random.randint(1,3))

resultado_pvp = f"""
Has elegido {lista[int(opcion_user)-1]}{opciones_juego[int(opcion_user)-1]}
EL pc a elegido {lista[int(opcion_pc)-1]}{[opcion_pc[int(opcion_pc)-1]]}
"""
print(resultado_pvp)
if opcion_user == opcion_pc:
    print("Empate")
elif (opcion_user == "1" and opcion_pc == "3") \
    or (opcion_user == "2" and opcion_pc == "1") \
        or (opcion_user == "3" and opcion_pc == "2"):
    print("¡¡¡Has ganado!!!")
else:
    print("¡¡¡Has perdido!!!")