#version 3.11

#Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista.

_getInputUser=''
_listaMedia=[]

def _startProgram():
    while True:
        _getInputUser=input("Introduzca un valor: ")

        try:
            _getInputUser=int(_getInputUser)
            _listaMedia.append(_getInputUser)
            _finish=input("¿Desea finalizar?(s/n): ")
            if _finish=='s':
                print(f"La media es {_CalculaMedia()}")
                break

        except ValueError:
            print("Solo se permiten valores enteros.")
            continue


def _CalculaMedia():
    
    suma=0
    for i in range(len(_listaMedia)):
        suma += int(_listaMedia[i])
    resultado =suma/len(_listaMedia)
    return round(float(resultado),2)


_startProgram()

