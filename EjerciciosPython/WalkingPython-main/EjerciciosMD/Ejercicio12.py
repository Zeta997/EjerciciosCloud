#version 3.11


#Dado un número entero, crea un algoritmo que determine si es primo o no.

_getInputUser=""
_arrayPrimos=[2,3,5,7,11,13,17,19,23]
_alamcenaPrimos=[]

def _startProgram():

    while True:
        _getInputUser=input("Introduce valores enteros: ")
        try:
            _getInputUser=int(_getInputUser)
            _CalculoPrimos(_getInputUser)
            _finish=input("¿Desea finalizar?(s/n): ")
            if _finish=='s':
                resultado=sorted(_alamcenaPrimos)
                print(f"Los valores primos son los siguiente: {resultado}")
                break
        except ValueError:
            print("No se permiten valores decimales o caracteres.")
            continue

def _CalculoPrimos(_value):
    for i in _arrayPrimos:
        resto= _value% i
        division= _value/ i
        if (resto!=0) and (division< i):
            _alamcenaPrimos.append(_value)
            break



_startProgram()
        
