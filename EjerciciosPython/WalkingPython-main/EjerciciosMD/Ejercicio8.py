#version 3.11

#Crea un algoritmo que determine si un año es bisiesto o no.


_getInputUser=""

def _startProgram():
    global _getInputUser

    while _getInputUser=="":
        _getInputUser=input("Introduce un año para determinar si es bisiesto o no: ")
        _CalculateYear(_getInputUser)



def _CalculateYear(_year):
    try:
        _year=int(_year)
        if(_year %400==0) or ((_year %4 ==0) and (_year%100!=0)):
            print(f"El año {_year} es bisiesto.")
        else:
            print(f"El año {_year} no es bisiesto.")

    except ValueError:
        print("No se permiten valores decimales o caracteres.")
        return _year==""

    
_startProgram()