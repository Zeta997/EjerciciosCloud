#version 3.11

#Dada una lista de nombres, crea un algoritmo que ordene la lista alfabéticamente.

_getInputUser=""
_listaName=[]

def _startProgram(_getInputUser):
    #global _getInputUser
    resultado=""
    while _getInputUser=="":
        _getInputUser=input("Introduce nombres: ")
        _listaName.append(_getInputUser)
        _finish=input("¿Desea finalizar el programa(si/no): ")
        if _finish=="si":
            resultado=sorted(_listaName)
            #print(_listaName)
        else:
            _getInputUser=""
    return resultado
res=_startProgram(_getInputUser) 
print(res)