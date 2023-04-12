#version 3.11

#Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida


_getInputTextString=""
listInverted=""
def _getInvertedText():
    global _getInputTextString, listInverted
    
    while _getInputTextString=="":
        _getInputTextString=input("Escribe una palabra o frase: ")
        
        for i in _getInputTextString:
            listInverted= i+ listInverted
        print(listInverted)    
    
        

_getInvertedText()

