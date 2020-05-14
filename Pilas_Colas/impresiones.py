import os
from collections import deque
from os.path import isfile, join, isdir
def Menu (): 
    print("""
    1) Agregar un elemento a la cola de impresion
    2) Imprimir
    3) Salir""")

cola=deque()

while True:
    Menu()
    seleccion=input("seleccie la operacion que se va a realizar: ")
    if seleccion=='1':
        print("ruta")
        ruta=input(">")
        contenido = os.listdir(ruta)
        archivos=[nombre for nombre in contenido if isfile(join(ruta, nombre))]
        lista=deque([archivos])
        print("Se encontraron los siguientes archivos en la carpeta actual: ")
        #for elemento in archivos:
        #   print(elemento)
        print ("=============================================================")
        print("Ingrese el numero de archivo que desea agregar a la cola: ")
        while len(lista) > 0:
            otra_lista= lista.popleft()
            for elemento , lista  in enumerate (otra_lista):
                indice=[elemento]
                lista=[indice, lista ]
                print(lista)
            sellections=int(input(":"))
            otra=otra_lista[sellections]
            cola.append(otra)
           
            print("La cola de impresion es:")
            for t in cola:
                print(f"{t}")
            break
    elif seleccion=='2':
        if len(cola) > 0:
            impresion = cola.popleft()
            lista=[impresion]
            print("------------------------------------")
            print(f'\nSe imprimio: {lista}')
            if len(cola) > 0:
                
                print("\nLa cola de impresion es:")
                print(cola)
                print("------------------------------------")
            else:
                while len(cola)==0:
                    print("------------------------------------")
                    print("\nLa cola de impresion esta Vacia")
                    print("------------------------------------")
                    break
        else:
            while len(cola)==0:
                print("------------------------------------")
                print("\nLa cola de impresion esta Vacia")
                print("------------------------------------")
                break
    elif seleccion =='3':
        break
    else:
        print("Opcion invalida...")
