#version 3.11

#Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista.

_getInputUser=''
_pares=[]

def _startProgram():
    while True:
        _getInputUser=input("Introduce valores: ")

        try:
            _getInputUser=int(_getInputUser)
            _CalcularPares(_getInputUser)
            _finish=input("¿Desea finalizar?(s/n): ")
            if _finish=='s':
                print(f"La suma de los numeros pares es: {_SumaPares()}")
                break
            
        except ValueError:
            print("Ha habido un error")
            return False




def _CalcularPares(_value):
    resto= _value %2
    if resto==0:
        _pares.append(_value)

def _SumaPares():
    resultado=0
    for i in range(len(_pares)):
        valor =int(_pares[i ])
        resultado +=valor
    return resultado

_startProgram()