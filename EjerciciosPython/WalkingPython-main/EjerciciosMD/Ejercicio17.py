#version 3.11

#Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.
import random
_getInputUser=''
_numRandom=0

def _startProgram():
    _numRandom=random.randint(1,100)
    while True:
        _getInputUser=input("Introduce un valor: ")
        try:
            _getInputUser=int(_getInputUser)

            if _getInputUser<_numRandom:
                print("El numero secreto es mayor")               
            elif _getInputUser>_numRandom:
                print("El numero secreto es menor")
            elif _getInputUser==_numRandom:
                print("Has acertado.")
                break    
        except ValueError:
            print("No se permiten decimales o caracteres")
            continue


_startProgram()