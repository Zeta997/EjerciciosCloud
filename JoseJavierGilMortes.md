# Ejercicios con algoritmos

### Ejercicio 1

Calcula la letra del DNI Español

**Paso 1:** Definir el problema

El numero del DNI debe tener 8 digitos, lo dividimos entre 23 y el resto sera el resultadoResto.
 El resultadoResto lo compararemos con la lista de codigos. 

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `DNI`, `resultadoResto`,   `resultado`

​	*Proceso:* Que el DNI tenga 8 digitos y que sean todos numéricos. 

​				   Si es erronea asigne a la variable resultado "DNI invalido

​					Dividimos DNI en 23 y el resto lo asignamos a resultadoResto

​					Comparar el resultadoResto con los valores de la tabla y asignar a letraDNI el valor equivalente en la tabla.

​	*Salida:* Imprime la letra del DNI 

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo DNI
		resultado->texto
    DNI ->Entrada de dato
    []letraDNI ->Almacenamiento de caracteres {T,R,W,A,G,M,Y,F,P,D,X,B,N,J,Z,S,Q,V,H,L,C,K,E}

    Si longitud DNI es distinto de 8 digitos 
        mostrar mensaje  resultado->"DNI invalido"
    sino
     resultadoResto<- valor obtenido por operacion
     resultadoResto<- DNI mod 23
     resultado <- letra[resultadoResto]

    fin condicion

    Mostrar mensaje "La letra de tu DNI es:" + resultado
    Fin Algoritmo
```



### Ejercicio 2

Calcula el salario de un empleado

**Paso 1:** Definir el problema

En España, para calcular el salario de un empleado se debe tener en cuenta el salario mínimo interprofesional (SMI), que es el salario más bajo permitido por ley. El SMI actual (2023) es de 1.100 euros brutos al mes, en 14 pagas. Para calcular el salario neto se deben considerar las deducciones de seguridad social y el impuesto sobre la renta de las personas físicas (IRPF). La tasa de contribución a la seguridad social es del 6,35% para los empleados y del 29,9% para los empleadores. El impuesto sobre la renta es progresivo y varía según los ingresos del empleado. Es importante verificar las políticas salariales de la empresa y las leyes laborales correspondientes.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `salario`,`salarioBase`,`salarioNeto`,`salarioBruto`, `pagaExtras`,   `complementos`,`otrosConceptosRetribuidos`, `IRPF`, `Seguridad Social`,`deducciones`

​	*Proceso:* El salarioBruto es la suma `salarioBase`, `pagaExtras`,   `complementos`,`otrosConceptosRetribuidos`.

​					Las deducciones son la suma de `IRPF`, `Seguridad Social`.

​					El salarioNeto es la resta de `salarioBruto`, `deducciones`

​	*Salida:*  Imprime `salarioBruto`, `salarioNeto`

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Salario
		salario <- leer()
		pagasExtras <- leer()
		complementos <- leer()
		otrosConceptosRetributivos <-leer()
		IRPF <-leer()
		Seguridad Social <-leer()
		
		salarioBruto <- salarioBase + pagasExtras+complementos+ otrosConceptosRetributivos
		salarioNeto<- salarioBruto - deducciones
		Imprime "El salario bruto es:" + salarioBruto
		Imprime "El salario neto es:" + salarioNeto
    Fin Algoritmo
```

### Ejercicio 3

Determinar la ruta para llegar a una ciudad por avión.

**Paso 1:** Definir el problema

El primer paso seria saber la localizacion tuya y la de destino, ver el aeropuerto mas proximo
a tu localizacion y el mas proximo a tu ciudad de destino, determinar que tipo de vuelo es, 
si es directo o con escala.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `ActualLocation`, `destinationLocation`,   `Airport`, `flightType`

​	*Proceso:* `ActualLocation` debe estar determinada por la localizacion del usuario.

​					 `destinationLocation` debe estar determinada por la agencia de vuelo.

​					 `Airport` determina el punto de inicio para llegar al destino.

​					 `FlightType` va a devolver el tipo de vuelo segun la preferencia del usuario y esta caracteristia viene determinada por la propia agencia.

*Salida:* Imprime el vuelo de partida y llegada con el tipo de vuelo

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Vuelo
		flightType{"directo", "transbordo"}
		actualLocation <- leer()
		destinationLocation <- leer()
		existLocation {"Alicante", "Valencia", "Barcelona", "Madrid"}
		existDestination {"Italia, "Francia", "Paises Bajos", "Alemania"}
		airport<-leer()
		
		funcion Princial()
		 si(ComparaLaLocalizacion y ComparaElDestino) entonces
		 	Imprime "Su vuelo desde "+actualLocation+" hasta "+destinationLocation+ "sera un vuelo "+flightType
		 sino
		 	Imprime "En estos momentos no hay vuelos disponibles."
		 	fin sentencia
		fin funcion
		
		funcion condicional ComparaLaLocalizacion()
			location <-- variable boolean
				Para i igual 0 i menor igual a la longitud existLocation menos 1 incrementar i en 1
						si (actualLocation es igual a existLocation) entonces
							Imprime "Aeropuerto disponible."
							location<- true "existe"
							existLocation igual a la longitud de existLocation
						fin sentencia
				fin bucle
				location <-false
				Imprime "No se ha encontrado el aeropuerto."
		fin funcion
		
		funcion condicional ComparaElDestino()
			location <-- variable boolean
				Para i igual 0 i menor igual a la longitud existDestination menos 1 incrementar i en 1
						si (destinationLocation es igual a existDestination) entonces
							Imprime "Vuelo disponible."
							location<- true "existe"
							existDestination igual a la longitud de existDestination
						fin sentencia
				fin bucle
				location <-false
				Imprime "No hay vuelo disponible."
		fin funcion
    Fin Algoritmo
```



### Ejercicio 4

Calcula el área y perímetro de un círculo dado su radio.

**Paso 1:** Definir el problema

Para calcular el area de un circulo necesitamos el valor del radio 
para aplicar la formula matematica a= pi*radio^2 y para el perimetro usaremos
p=2*pi*radio 

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `radio`, `PI`

​	*Proceso:* Definimos el valor de Pi, mientras que el valor del Radio lo obtenemos con el Input de usuario.

*Salida:* Imprime el valor del área y perímetro 

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Area y Perimetro
		
		PI <- constante definida "3,141592"
		radio <- leer()
		
	funcion principal()
			
    Imprime "Por favor ingrese el valor del radio del circulo."
    Calculo(radio)
  fin funcion


  funcion void Calculo(recibe valor valorACalcular)

    #calculoA igual a Pi por valorACalcular elevado a 2
    #calculoP igual a 2 por Pi por valorACalcular
    Imprime "El area del circulo es: "+ calculoA
    Imprime "El perimetro del circulo es: "+calculoP
  fin funcion
  
    Fin Algoritmo
```



### Ejercicio 5

Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor.

**Paso 1:** Definir el problema

Para determinar el mayor y el menor creamos un array con varios datos de tipo entero 
creamos un bucle en el que obtengamos todos los valores del array y los vamos comparando 1 a 1 con el condicional de tal manera que podamos ir agrupando en una lista los valores de menor a mayor.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `cadenaEnteros`,  `listaOrdenada` 

​	*Proceso:* Creamos 2 bucles uno para validar todos los valores dentro del array de cadenaEnteros y el segundo para comparar los valores de tal manera que los comparamos con un condicionar para crear una listaOrdenada y agruparlos de menor a mayor.

*Salida:* Imprime los valores de listaOrdenada

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Menor Mayor
		cadenaEnteros {100,3,5,8,14,2,30}
		listaOrdenada[]
		
		Para i igual 0 i menor igual a la longitud cadenaEnteros menos 1 incrementar i en 1
		
			Para j igual 1 mas i j menor igual a la longitud cadenaEnteros menos 1 incrementar j en 1
			
				si (cadenaEnteros[i] menor a cadenaEnteros[j]) entonces
					añade a listaOrdenada[i]
					cadenaEnteros igual a longitud cadenaEnteros -1
				fin sentencia
				
		 fin bucle
		
		fin bucle
  	Imprime listaOrdenada
    Fin Algoritmo
```

### Ejercicio 6

Crea un algoritmo que convierta grados Celsius a Fahrenheit.

**Paso 1:** Definir el problema

Para convertir grados Celsius a Fahrenheit nos basamos en la formula (grados *9/5)+32.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `grados`

​	*Proceso:* Obtenemos el valor de Grados por el input del usuario y lo aplicamos a la formula.

*Salida: Imprimimos por pantalla La conversion.

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Grados Cel a Fahrenheit
		grados <--Input User
		
    conversion= (grados * 9/5)+32;
    Imprime grados+" C en Fahrenheit son: " + conversion+" F."
    
    Fin Algoritmo
```



### Ejercicio 7

Dado un número entero, crea un algoritmo que determine si es par o impar.

**Paso 1:** Definir el problema

Para saber si un numero es par o impar basta con saber si el resto de la division es 0.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `num`

​	*Proceso:* Cogemos el valor de `num` y lo dividimos entre 2 si el resto da 0 es par y sino es impar.

*Salida: Imprime "par" "impar"

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Par Impar
		num <- leer()

    si(num mod 2 es igual 0) entonces
        Imprime num +" es par"
    sino 
        Imprime num +" es impar"
    
    Fin Algoritmo
```

### Ejercicio 8

Crea un algoritmo que determine si un año es bisiesto o no.

**Paso 1:** Definir el problema

Para saber si un año es bisiesto o no deberemos coger el valor del usuario y a través de unas sentencias determinar si es bisiesto o no.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `num`

​	*Proceso:* Con la condicion dividimos  `num` entre 400 si el resto es 0 es bisiesto o dividimos el  `num` entre 4 y 100 y si entre 4 da 0 					y 100 distinto de 0 es bisiesto. sino no es bisiesto.

*Salida: Imprime "Es bisiesto"

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Bisiesto
		num <-leer()

    si( 
        (num mod 400 igual a 0) o 
        ( (num mod 4 igual a 0) y (num mod 100 diferente a 0) ) 
       )

        resultado<- num+" es bisiesto"

    sino 

        resultado<- num+" no es bisiesto"

    fin sentencia

    imprime resultado
    Fin Algoritmo
```

### Ejercicio 9

Crea un algoritmo que determine si una cadena de texto es un palíndromo o no.

**Paso 1:** Definir el problema

Para saber si una cadena de texto es un palíndromo, es necesario comprobar si la cadena se lee igual de izquierda a derecha que de derecha a izquierda. 

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `cadena`

​	*Proceso:* Elimina cualquier espacio en blanco y convierte todos los caracteres a minúsculas (o mayúsculas) para que las comparaciones sean insensibles a mayúsculas y minúsculas.

​				  Crea una copia de la cadena original y invierte el orden de sus caracteres.

​				 Compara la cadena original con su copia invertida. Si son iguales, entonces la cadena es un palíndromo.

*Salida: Imprime "La cadena es palíndromo"

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Palindromo

   cadena <- leer()

   #cadena <- Convertir a minúsculas y eliminar espacios en blanco
   reversa <- depuracionCadena(cadena)
   
   Si cadena es igual a reversa entonces
     resultado <- "La cadena es un palíndromo"
   Sino
     resultado <- "La cadena no es un palíndromo"
   Fin Si

   escribir resultado
Fin Algoritmo

funcion depuracionCadena (cadena)
    #quita los espacios en blanco, otros caracteres y convierte todo a minusculas
    i<-0
    Mientras cadena[i] sea diferente de findecadena Haga
        caracter<-""
        Si  el ASCII de cadena[i]  mayor que 64 y ASCII de cadena[i] menor que 91 Entonces
            caracter<-cadena[i] en minusculas
        Fin Si
        Si  el ASCII de cadena[i]  mayor que 96 y ASCII de cadena[i] menor que 123 Entonces
            caracter<-cadena[i]
        End Si
        temporal <- temporal + caracter
        Si caracter es diferente "" Entonces
            i<-i+1
        Fin Si
    Fin Mientras
    L<-i
    reversa<-""
    Para N = 0 Hasta L-1 Con Paso 1 Haga
        reversa    <-reversa+ temporal[i-1]
        i<-i-1
    Fin Para
    devuelva reversa
Fin funcion
```

### Ejercicio 10

Dada una lista de nombres, crea un algoritmo que ordene la lista alfabéticamente.

**Paso 1:** Definir el problema



**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `cadena`

​	*Proceso:* Elimina cualquier espacio en blanco y convierte todos los caracteres a minúsculas (o mayúsculas) para que las comparaciones sean insensibles a mayúsculas y minúsculas.

​				  Crea una copia de la cadena original y invierte el orden de sus caracteres.

​				 Compara la cadena original con su copia invertida. Si son iguales, entonces la cadena es un palíndromo.

*Salida: Imprime "La cadena es palíndromo"

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo lista alfabetica

   lista[] <-leer()
numero<--ContarElementos(lista)
listaOrdenada <- lista
j<-0

Repetir
    menorPalabra <-- lista
    Para i igual j hasta n menos 1 paso 1 hacer
        Si menorPalabra es mayor que listaOrdenada[i]
        	posicion <- i 
        Fin sentencia 
    Fin bucle
    temporal <-- listOrdenada[j]
    listaOrdenada[j]<-- menorPalabra
    listaOrdenada[posicion]<- temporal
    j<- j=1
Hasta que j sea igual que n

Imprime listaOrdenada

Fin Algoritmo
```

### Ejercicio 11

Crea un algoritmo que calcule el factorial de un número entero.

**Paso 1:** Definir el problema

El factorial de un número es el producto de todos los números enteros positivos desde 1 hasta ese número. 

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `numero`, `factorial`

​	*Proceso:* Con un bucle obtenemos los valores decrementados que el usuario introduzca, los almacenamos en un array y calculamos su factorial.

 *Salida:* Imprime  el factorial del numero.

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo factorial
numero <-leer()
factorial[]
calcularFact
Para i igual numero i mayor igual 0 decrementa i en 1
    restar 1 a numero

    facotrial[i] igual a numero
Fin bucle 

Para j igual 0 i menor igual longitud factorial incrementa i en 1

	calcularFact igual a multiplicar valores de factorial[j]
	
Fin bucle 

Imprime "El factorial es: "+ calcularFact
Fin Algoritmo
```

### Ejercicio 12

Dado un número entero, crea un algoritmo que determine si es primo o no.

**Paso 1:** Definir el problema

Para saber si un número es primo o no, debes comprobar si tiene exactamente dos divisores distintos: 1 y el propio número. Es decir, que no puede ser divisible por ningún otro número entero distinto de 1 y de sí mismo.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `numero`, `arrayPrimos`

​	*Proceso:* Obtenemos el numero del usuario y creamos un bucle, ese bucle se encargara de obtener el resto entre el valor introducido y los valores del array, si alguno de ellos coincide con la sentencia sera primo sino no lo sera.

 *Salida:* Imprime  "Es primo" "No es primo".

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Primo
numero <-leer()

arrayPrimos[]{2,3,5,7,11,13,17,19,23}

Para i igual 0 i menor igual longitud arrayPrimos incrementa i 1

    division <- numero mod arrayPrimos[i]

    si ((division es distinto 0) y (cociente es menor arrayPrimos[i]))
        Imprime "Es primo"
    fin sentencia
Fin bucle

Imprime "No es primo."
Fin Algoritmo
```

### Ejercicio 13

Crea un algoritmo que calcule el área y volumen de un cubo dado su lado.

**Paso 1:** Definir el problema

El área y el volumen de un cubo dependen de la longitud de sus lados.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `numero`

​	*Proceso:* aplicamos el valor introducido por el usuario en sus respectivas formulas ya definidas. La fórmula del área de un cubo es A = 6L^2, donde L es la longitud de uno de los lados del cubo. La fórmula del volumen de un cubo es V = L^3.

 *Salida:* Imprime  el valor de ambos resultados.

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Area y Volumen
numero <-leer()

calculoArea igual a 6 por numero elevado 2
calculoVolumen igual a numero  elevado 3

Imprime "El area del cuadrado es: "+ calculoArea
Imprime "El volumen del cuadrado es: "+ calculoVolumen
Fin Algoritmo
```

### Ejercicio 14

Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista.

**Paso 1:** Definir el problema

Queremos tener los elementos pares de un array y sumarlos para obtener el resultado.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `listaNumeroEntero`, `listaNumerosPares`, `resultado`

​	*Proceso:* Creamos una array listaNumerosEnteros que almacene los datos que el ususario introduzca y creamos un bucle que compruebe cada una de las posiciones dentro de ese bucle creamos una sentencia que compruebe el resto de cada valor si es 0 lo añadimos a la listaNumerosPares. Despues cogemos los valores y los sumamos todos obteniendo el resultado de la suma de todos los pares.

​	*Salida:*  Imprime  el valor de ambos resultados.

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo ParesLista
listaNumerosEnteros[] <-leer()

listaNumerosPares[]

resultado

Para i igual 0 i menor o igual a longitud ListaNumeroEntero -1 suma 1 a i 

    Si listaNumeroEntero[i] mod 2 es igual 0 entonces

     	añade listaNumeroEntero[i] a listaNumerosPares;

    fin sentencia

Fin bucle

Para a igual 1 a menor o igual a longitud ListaNumeroEntero -1 suma 1 a a 
    
    resultado <-- suma todos los valores de listaNumerosPares[a]

Fin bucle

    Imprime "El resultado de la suma de los numeros pares es: "+ resultado
Fin Algoritmo
```

### Ejercicio 15

Crea un algoritmo que determine si un número es positivo, negativo o cero.

**Paso 1:** Definir el problema

Tenemos que detectar el valor que ha introducido el usuario y determinar si es positivo, negativo o 0.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `valorIntroducido`

​	*Proceso:* Una vez se obtenga el valor introducido se compara con las sentencias determinando el tipo de dato introducido(positivo, negativo, 0).

​	*Salida:* Imprime por pantalla el resultado con un mensaje.

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo TipoDeDato
valorIntroducido <-leer()

Si valorIntroducido es menor 0 entonces

	resultado <--valorIntroducido
	Imprime "El valor introducido "+resultado+" es negativo"

Sino si valorIntroducido es igual 0 entonces

	resultado <--valorIntroducido
	Imprime "El valor introducido "+resultado+" es 0"

Sino si  valorIntroducido es mayor 0 entonces

	resultado <--valorIntroducido
	Imprime "El valor introducido "+resultado+" es positivo"

Fin sentencia

Fin Algoritmo
```

### Ejercicio 16

Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista.

**Paso 1:** Definir el problema

Para calcular la media de un conjunto de números, debes sumar todos los números y luego dividir la suma por la cantidad de números. 

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `listaNumero`, `sumValores`, `resultado`

​	*Proceso:* creamos un bucle que repase todos los elementos del array y que acada elemento lo sume con el siguiente para obtener la suma de todos los elemento del array. Seguidamente dividimos  `sumValores` entre el total del array, es decir, el total de elementos que se compone el array obteniendo la media.

​	*Salida:* Imprime por pantalla el resultado con un mensaje.

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Media
listaDeNumero[]<--Input User
sumValores
resultado

Para i igual 0 i menor igual que longitud de listaDeNumero -1 sumamos 1 a i

	
	sumaValores <-- suma listaDeNumeros[i]

Fin bucle

Resultado<-- sumaValores/ longitud listaDeNumeros

Imprime "La media es: "+ resultado
Fin Algoritmo
```

### Ejercicio 17

Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.

**Paso 1:** Definir el problema

Generar un numero aleatorio que viene dada por un subalgoritmo que genera la maquina, leemos el valor que el usuario ha introducido y lo comparamos con el valor que ha generado la maquina.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `numeroRandon`, `numeroSelect`

​	*Proceso:* Necesitamos crear una variable para generar el numero random y otra variable para obtener el valor del usuario. Creamos un bucle con la condición de que los valores no coincidan y a través de las sentencias guiamos al usuario de si el valor es mayor o menor.

​	*Salida:* Imprime por pantalla si el valor es mayor, menor o si ha acertado.

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo NumeroAleatorio
numeroRandon <- Rango(1,100) <--metodo clase

numeroSelec <-leer()


Mientras numeroSelec sea distinto de numeroRando ejecuta lo de abajo

Si numeroSelec es menor a numeroRandon entonces

	Imprime "El numero secreto es mayor."

Sino si numeroSelec es mayor a numeroRandon entonces

	Imprime "El numero secreto es menor."


Fin bucle

Imprime "Has adivinado el numero secreto."
Fin Algoritmo
```

### Ejercicio 18

Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto.

**Paso 1:** Definir el problema

Una cadena de texto es un anagrama de otra cadena si se pueden reorganizar las letras de la primera cadena para formar la segunda cadena. Por ejemplo, "roma" es un anagrama de "amor".

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `cadenaUno`, `cadenaDos`

​	*Proceso:*  Para determinar si dos cadenas de texto son anagramas, debemos comprobar si tienen las mismas letras, independientemente del orden. Podemos hacer esto convirtiendo ambas cadenas en listas de caracteres, ordenando cada lista y luego comparándolas. Si las dos listas son iguales, entonces las cadenas son anagramas.

​	*Salida:* Imprime si es anagrama o no.

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo Anagrama
cadenaUno <-leer()
cadenaDos <- leer()
n<-ContarElementosLista(cadenaUno)
m<-ContarElementosLista(cadenaDos)
si n es igual a m
	i<-0
	resultado<- "es anagrama"
	Mientras i sea menos o igual que n menos 1
		noEstaLetra<- true
		Para j igual i hasta n menos 1 con paso 1 hacer
			sicadenaUno[i] es igual a cadena2[j]
			poscion <- j
			noEstaLetra <- false
		fin bucle
		si noEstaLetra es igual a true entonces
			resultado <-"no es anagrama"
			i<- n
		sino
			temporal <- cadenaDos[i]
			cadenaDos[i]<- cadena2[i]
			cadenaDos[posicion]<- temporal
			i <- i mas 1
		fin sentencia
	fin bucle princial
fin sentencial principal
resultado <- "no es anagrama"
Fin Algoritmo
```

### Ejercicio 19

Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la
lista.

**Paso 1:** Definir el problema

Crear un algoritmo que elimine los repetidos de la lista.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `listaNumeroEntero`, `listaSinDuplicar`

​	*Proceso:* Creamos un array con elementos enteros y una lista donde almacenaremos los valores que no se repiten. Hacemos un bucle que recorra todo el array de listaNumeroEntero y a través de la condicionante añadimos el valor a la listaSinDuplicar o lo eliminamos.

​	*Salida:* Imprimimos los valores de listaSinDuplicar.

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo NumeroAleatorio
listaNumeroEntero[] {3,3,6,9,5,1,3}
listaSinDuplicar[]

 Para i igual 0 i menor o igual a longitud listaNumeroEntero -1 sumamos 1 i 

	Para a igual 1 mas i; a menor o igual longitud listaNumeroEntero -1 sumamos 1 a

		si listaNumeroEntero i igual listaNumeroEntero a
			Elimina elemento de listaNumeroEntero
		 i igual longitud de listaNumeroEntero -1;
	fin segundo bucle

	añade listaNumeroEntero con elemento a ->listaSinDuplicar

Fin primer bucle

Imprime listaSinDuplicar
Fin Algoritmo
```

### Ejercicio 20

Crea un algoritmo que determine si un número es capicúa o no.

**Paso 1:** Definir el problema

Un número es capicúa si se lee igual de izquierda a derecha que de derecha a izquierda. Por ejemplo, 121 es un número capicúa porque se lee igual en ambas direcciones.

**Paso 2:** Poner la entrada, el proceso y la salida

​	Entrada: `numero`

​	*Proceso:* cogemos el valor lo cambiamos a texto y a traves de ambos bucles comparamos las cadenas y si ambas mitades coinciden el valor sera capicua y sino no lo sera.

​	*Salida:* Imprime si es capicua o no.

**Paso 3:** Escribir el pseudocódigo

```
		Algoritmo NumeroAleatorio
numero <-leer()

funcion es_capicua(numero):
    # Paso 1
    numeroString[]<- convertimos numero en texto
    
    # Paso 2
    longitud <- longitud numeroString
    
    # Paso 3
    Para i igual 0  i menor igual longitud dividido entre 2 incrementa i 1 
        # Paso 4

        j <-- longitud - i - 1
        
        # Paso 5
        Si numeroString[i] es distinto de numeroString[j] entonces
            Imprime "No es capicua"
    		fin sentencia
    # Paso 6
    Imprime "Es capicua"

Fin Algoritmo
```

