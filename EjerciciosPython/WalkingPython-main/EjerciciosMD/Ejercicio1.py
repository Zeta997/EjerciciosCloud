#version 3.11

#Calcular la letra del DNI Español

_listString=["T", "R",	"W",	"A",	"G",	"M",	"Y",	"F",	"P",	"D",	"X",	"B",	"N",	"J",	"Z", 	"S",	"Q", 	"V",	"H",	"L",	"C", 	"K",	"E"]

_getInputUser=""

def _startProgram():
    global _getInputUser

    while _getInputUser=="":
        _getInputUser=input("Introduce tu DNI numerico: ")
        
        if len(_getInputUser) !=8:
            print("Debes introducir 8 digitos")
            _getInputUser=""
        else:

            _CalculoDNI()


def _CalculoDNI():
    global _getInputUser
    _getInputUser=int(_getInputUser)
    calculo= _getInputUser % 23
    print(f"La letra de tu DNI es: {_getInputUser}{_listString[int(calculo)]}")


_startProgram()