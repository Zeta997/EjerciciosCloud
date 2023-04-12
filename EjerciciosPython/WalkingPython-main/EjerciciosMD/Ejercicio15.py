#version 3.11

#Crea un algoritmo que determine si un número es positivo, negativo o cero.

_getInputUser=''

def _startProgram():
    while True:
        _getInputUser=input("Introduce un valor: ")
        try:
            _getInputUser=int(_getInputUser)
            _DeterminarNumero(_getInputUser)
            break
        except ValueError:
            print('Ha habido un error.')
            break


def _DeterminarNumero(_value):
    if _value<0:
        print(f'El numero {_value} es negativo')
    elif _value==0:
        print(f'El numero {_value} es 0')
    elif _value>0:
        print(f'El numero {_value} es positivo')

_startProgram()