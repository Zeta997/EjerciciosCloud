#version 3.11

#Crea un algoritmo que determine si una cadena de texto es un palíndromo o no.


_getInputUser=""
_lista1=[]
_lista2=[]

def _startProgram():
    global _getInputUser

    while _getInputUser=="":
        _getInputUser=input("Introdude una palabra: ")
        _lista1=list(_getInputUser)
        _getInputUser=input("Introdude otra palabra: ")
        _lista2=list(_getInputUser)

        _lista1.sort()
        _lista2.sort()

        if _lista1==_lista2:
            print("Es palíndromo")
        else:
            print("No es palíndromo")

_startProgram()