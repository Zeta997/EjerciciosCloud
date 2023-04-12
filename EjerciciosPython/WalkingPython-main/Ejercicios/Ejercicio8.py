#version 3.11

#Crea un programa en Python que acepte una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que tienen más de 5 caracteres.

_getStringUser=""
listStringMoreFive=[]
listString=[]
_getNumberOfString=""
_finishInstruction=False

def _GetStringUser():
    global _getStringUser, _finishInstruction

    while _finishInstruction==False:
        _getStringUser=input("Introduce una frase o palabra: ")
        _ConditionsToWork()

        
        

def _CompareText():
        for i in listString:
            _getNumberOfString=i
            if len(_getNumberOfString)>= 5:
                listStringMoreFive.append(_getNumberOfString)
            else:
                continue

def _ConditionsToWork():

        global _getStringUser, _finishInstruction
        _getStringUser= str(_getStringUser)
        listString.append(_getStringUser)
        _finishProgram=input("¿Desea finalizar?(si/no): ")
            
        if _finishProgram=="si":
            _finishInstruction=True
            _CompareText()  
            if listStringMoreFive==[]:
                    print("La lista está vacía")
            else:
                    print(listStringMoreFive)





_GetStringUser()



            