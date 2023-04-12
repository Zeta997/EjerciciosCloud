#version 3.11

#Dado un número entero, crea un algoritmo que determine si es par o impar.

_getInputUser=""

def _startProgram():
    global _getInputUser
    
    while _getInputUser=="":

        _getInputUser=input("Introduce un valor: ")

        try:
            _getInputUser=int(_getInputUser)

            if _getInputUser % 2==0:
                print("Es par")
                break
            else:
                print("Es impar")
                break

        except ValueError:
            try:
                _getInputUser=float(_getInputUser)
                if _getInputUser % 2==0:
                    print("Es par")
                    
                else:
                    print("Es impar")

            except ValueError:
                print("Ha habido un error.")
                _getInputUser=""


_startProgram()
