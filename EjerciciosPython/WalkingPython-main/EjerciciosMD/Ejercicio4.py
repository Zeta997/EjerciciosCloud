#version 3.11

#Calcula el área y perímetro de un círculo dado su radio.

import math

_pi=math.pi

_getInputUser=""

def _startProgram():
    global _getInputUser

    while _getInputUser=="":
        _getInputUser=input("Introduce el radio del circulo: ")
        try:
            _getInputUser=int(_getInputUser)
            _CalculoRadio(_getInputUser)
            
        except ValueError:
            try:
                _getInputUser=float(_getInputUser)
                _CalculoRadio(_getInputUser)
            except:
                print("Error durante el proceso, intentelo de nuevo.")
                _getInputUser=""

        
            


def _CalculoRadio( value):
    _calculoA= _pi*pow(value,2)
    _calculoP= 2*_pi*value
    print(f"El área del circulo es: {round(_calculoA,2)}")
    print(f"El perimetro del circulo es: {round(_calculoP,2)}")


_startProgram()