#version 3.11

#Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor.

_cadenaEnteros=[]
_listaOrdenada=[]
_getINputUser=""
_finishProgram=""


def _startProgram():
    global _getINputUser, _finishProgram
    
    while _getINputUser=="":
        _getINputUser=input("Introduce valores: ")
        try: 
            _getINputUser=int(_getINputUser)
            _cadenaEnteros.append(_getINputUser)
            _finishProgram= input("¿Desea finalizar el programa?")
            if _finishProgram=="si":       
                _DetecNumber()
            else:
                _getINputUser=""
        except ValueError:
            try:
                _getINputUser=float(_getINputUser)
                _cadenaEnteros.append(_getINputUser)  
                if _finishProgram=="si":       
                    _DetecNumber()
                else:
                    _getINputUser=""
            except:
                print("Solo se permiten valore enteros o decimales")
                _getINputUser=""

def _DetecNumber():
    _cadenaEnteros.sort()
    print(_cadenaEnteros)

            
            
_startProgram()