#version 3.11

#Crea un programa que le pida al usuario un número entero y luego calcule y muestre la suma de todos los números desde 1 hasta el número ingresado.
_totalValor=0
_valor=""

while _valor=="":
    
    _valor=input("Introduce un valor: ")

    try:
   
        _valor=int(_valor)
    
        for i in range(_valor,-1,-1):

            _totalValor +=i

        print(f"La suma total del numero introducio es: {_totalValor}")

    except ValueError: 
        
        print("Debes introducir un valor entero.")
        _valor=""
