"""
Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a
Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py.
"""



def estaEnRango(valor, minimo, maximo):


    try:
        if valor >= minimo and valor <= maximo:
            return True
        else:
            return False
    except IndentationError:
        print("Error... El número no está entre 1 y 20")
        return False




def estaEnLista(valor, lista):


    try:
        if valor in lista:
            return True
        else:
            return False
    except IndentationError:
        print("Error... El número no está en la lista")
        return False



min=1
max=20
num=int(input(f"Escribe un número entre 1 y 20 "))
lista=[6,14,11,3,2,1,15,19]




if estaEnRango(num, min, max):

    try:        
        if estaEnLista(num, lista):
            print(f"¡Bien! {num} está en la lista")
        else:
            print(f"El número {num} que has introducido está en el rango pero no está en la lista. Intenta de nuevo")
    except IndentationError:
        print("ERROR...")
else:
    print(f"{num} no se encuentra entre {min} y {max}" )
