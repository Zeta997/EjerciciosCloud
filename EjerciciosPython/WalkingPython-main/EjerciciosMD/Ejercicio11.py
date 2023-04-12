#version 3.11

#Crea un algoritmo que calcule el factorial de un número entero.
import math
_getInputUser=""

def _starProgram():
    global _getInputUser

    while _getInputUser=="":
        _getInputUser=input("Introduce un numero: ")
        try: 
            _getInputUser=int(_getInputUser)
            _factorial = math.factorial(_getInputUser)
            print(f"El factorial de {_getInputUser} es {_factorial}")
        except ValueError:
            print("Solo se permiten valores enteros.")
            _getInputUser=''

_starProgram()