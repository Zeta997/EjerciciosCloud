#version 3.11

#Crea un algoritmo que calcule el área y volumen de un cubo dado su lado.
import math
_getInputUser=''

def _startProgram():
    while True:
        _getInputUser=input("Introduce un valor: ")
        try:
            _getInputUser=int(_getInputUser)
            _CalculoAyV(_getInputUser)
            break          
        except:
            try:
                _getInputUser=float(_getInputUser)
                _CalculoAyV(_getInputUser)
                break
            except ValueError:
                print("Ha habido un error")
                return False
            



def _CalculoAyV(_value):
    _calculoA= 6*math.pow(_value,2)
    _calculoV=math.pow(_value,3)
    print(f"El area del cubo es: {round(_calculoA,2)}")
    print(f"El volument del cubo es: {round(_calculoV,2)}")

_startProgram()