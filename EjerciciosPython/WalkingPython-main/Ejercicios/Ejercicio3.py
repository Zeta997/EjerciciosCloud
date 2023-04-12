#version 3.11

#Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene.

def _GetNumberCharacter():
    _inputString=""
    x=0
    while _inputString=="":
        _inputString=input("Introduce un mensaje ")
        for i in _inputString:
            if i.isspace():
                continue
            else:
                x+=1
        
    print(f"La cadena tiene un total de {x} palabras")

_GetNumberCharacter()