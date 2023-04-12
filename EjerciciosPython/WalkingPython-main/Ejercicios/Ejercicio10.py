#version3.11

#Crea un un programa en Python que tome una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que contienen al menos una vocal.


_getStringInputUser=""
_listVowel=['a','e','i','o','u','A','E','I','O','U']
_listAllString=[]
_listStringWithVowel=[]
_endProgram=False

def _GetInputUser():
    global _getStringInputUser
    
    while _endProgram:
        _getStringInputUser= input("Introduce una cadena de caracteres o frase: ")
        _listAllString.append(_getStringInputUser)
        _CompareVowel()
        _FinishProgram()
        


def _CompareVowel():
    _addString=""
    for i in _listAllString:
        _addString=i
        for a in _addString[0:]:
            for e in _listVowel[0:]:
                if a==e:
                    _listStringWithVowel.append(_addString)
                    break
                
            
def _FinishProgram():
    global _endProgram
    _getInputUser=input("¿Quieres finalizar el programa(si/no): ")
    if _getInputUser== "si":
        _endProgram=True
    elif _getInputUser=="no":
        _endProgram=False



_GetInputUser()  
    



