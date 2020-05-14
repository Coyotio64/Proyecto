from random import*
from collections import deque
historial1=deque()
historial2=deque()
historial3=deque()
def opcionJugador():
    print("\nElige tu respuesta: ")
    print("""  
    1). Piedra
    2). Papel
    3). Tijera """)
    opcion = int(input("==> "))
    if opcion == 1:
        historial1.append("PIEDRA")
        return "PIEDRA"
        
    elif opcion == 2:
        historial1.append("PAPEL")
        return "PAPEL"
    elif opcion == 3:
        historial1.append("TIJERA")
        return "TIJERA"
    else:
        print("Opcion invalida...")


def opcionMaquina():
    opcion = randint(1, 3)
    if opcion == 1:
        historial2.append("PIEDRA")
        return "PIEDRA"
    elif opcion == 2:
        historial2.append("PAPEL")
        return "PAPEL"
    elif opcion == 3:
        historial1.append("TIJERA")
        return "TIJERA"
    else:
        print("Opcion invalida...")
# Se define el ganador
def ganador(player, pc):
    if player == pc:
        historial3.append("EMPATE")
        return "EMPATE"
 # -----------------------------
    if player == "PIEDRA" and pc == "PAPEL":
        historial3.append("Gana Computadora!")
        return " Gana Computadora!"
    if player == "PIEDRA" and pc == "TIJERA":
        historial3.append("Gana Humano!")
        return "Gana Humano!"
 # -----------------------------
    if player == "PAPEL" and pc == "PIEDRA":
        historial3.append("Gana Humano!")
        return "Gana Humano!"
    if player == "PAPEL" and pc == "TIJERA":
        historial3.append("Gana Computadora!")
        return "Gana Computadora!"
 # -----------------------------
    if player == "TIJERA" and pc == "PIEDRA":
        historial3.append("Gana Computadora!")
        return "Gana Computadora!!"
    if player == "TIJERA" and pc == "PAPEL":
        historial3.append("Gana Humano!")
        return "Gana Humano!"
   
# Muestra el resultado
def resultado():
    historial= deque()
    j = opcionJugador()
    m = opcionMaquina()
    g = ganador(j, m)
    lista=[f'Computadora: {m}',f'Humano: {j}',f'Resulatado: {g}']
    historial=deque([lista])
    for elemento in lista:
        print(elemento)
    while True:
        print("""  
        Deseas?:
        1)Jugar de nuevo
        2)Ver resultado anterior
        3)Salir""")
        opcionFinal=input()
        if opcionFinal=='1':
           resultado()

        elif opcionFinal=='2': #lista1=deque([lista])
            if len(historial1) > 0:
                while len(historial1) > 0:
                    accion1= historial1.pop()
                    accion2=historial2.pop()
                    accion3=historial3.pop()
                    print(f'\nComputadora: {accion2}')
                    print(f'Humano: {accion1}')
                    print(f'Resultado: {accion3}')
                    break
            else:
                 while len(historial1)==0:
                    print("\n¡El Historial esta Vacio!")
                    break
                
        elif opcionFinal=='3':
            break
        else:
            print("Seleccione una opcion valida...")
    print('====================================================')
  
resultado()

