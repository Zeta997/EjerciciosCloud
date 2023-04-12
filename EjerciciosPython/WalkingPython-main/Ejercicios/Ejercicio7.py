#version 3.11

#Crea un programa que le pida al usuario una cadena de caracteres y luego imprima cada carácter en una línea separada. 

_getStringUser=""

while _getStringUser=="":
    _getStringUser=input("Introduce una frase o palabra: ")
    for i in _getStringUser:
        print(i)
