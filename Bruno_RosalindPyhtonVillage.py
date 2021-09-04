#Bruno Villalobos Reveles.
#18/08/21
#Ejercicios de Python Village Rosalind.


#Variables y algo de aritmetica.

a = int(input('Inserte el valor de a: ')) #Se define el primer entero.
b = int(input('Inserte el valor de b: ')) #Se define el segundo entero.
print(f'{a}^2 + {b}^2 = {a**2 + b**2}') #Se realiza e imprime la operacioón.

#Strings y Listas.

InicioPrimeraPalabra = int(input('Inserte el inicio de la primera palabra: ')) #Se piden los limites de las dos palabras a imprimir.
FinalPrimeraPalabra = int(input('Inserte el final de la primera palabra: '))
InicioSegundaPalabra = int(input('Inserte el inicio de la seunda palabra: '))
FinalSegundaPalabra = int(input('Inserte el final de la segunda palabra: '))
TextoStr = input('Inserte el texto e input: ')
print( f'{TextoStr[InicioPrimeraPalabra:FinalPrimeraPalabra + 1]} {TextoStr[InicioSegundaPalabra:FinalSegundaPalabra + 1]}')

#Condiciones y Loops.

NumeroInicial = int(input('Inserte el numero inicial: ')) #Se pide el rango de numeros en torno al que se sumara.
NumeroFinal = int(input('Inserte el numero final: '))
resultado = 0

for i in range(NumeroInicial, NumeroFinal + 1):  #Se realiza el ciclo para sumar todos los nones.
    if i % 2 != 0:
        resultado += i

print(resultado)                                 #Se imprime el resultado.

#Trabajando con Archivos.

output = []                                     #Definimos el output como una lista.

with open('inputRosalind.txt', 'r') as f:       #Abrimos y leemos el archivo, contamos el numero de palabras, y agregamos las necesarias a la lista.
    output = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]

with open('outputRosalind', 'w') as f:          #Escribimos un nuevo archivo con el contenido de la lista output[].
    f.write (''.join([line for line in output]))

#Diccionarios.

txtStr = input('Inserte el string de entrada:') #Definimos los parametros necesarios.
DictOutput = {}

for word in txtStr.split (' '):  #Vamos recorriendo las palabras, y se le agrega un numero dependiendo de cuantas veces aparezca en el output.
    if word in DictOutput:
        DictOutput[word] += 1
    else:
        DictOutput[word] = 1 

for key,value in DictOutput.items():    #Se imprime la llave y su valor. 
    print(key,value)


