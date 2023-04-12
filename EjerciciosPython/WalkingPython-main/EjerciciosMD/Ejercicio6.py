#version 3.11

#Crea un algoritmo que convierta grados Celsius a Fahrenheit.

_getInputUser=""

def _startProgram():
    global _getInputUser

    while _getInputUser=="":

        _getInputUser=input("Introduce los grados: ")

        try: 
            _getInputUser=int(_getInputUser)
            if _getInputUser in range(-60, 50):
                conversion = (_getInputUser*9/5)+32
                print(f"La temperatura de {_getInputUser} C son {conversion} F.")
            else:
                print("Introduzca valores coherentes.")
                _getInputUser=""
        except:
            
            _getInputUser=float(_getInputUser)
            if _getInputUser in range(-60, 50):
                conversion = (_getInputUser*9/5)+32
                print(f"La temperatura de {_getInputUser} C son {conversion} F.")
            else:
                print("Introduzca valores coherentes.")
                _getInputUser=""


_startProgram()