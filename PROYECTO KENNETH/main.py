import Proyecto.validaciones as val
import Proyecto.encriptado as crypt

valint=val.valint
valfloat=val.valfloat
valcomplex=val.valcomplex
vallist=val.vallist

encriptar=crypt.encriptar
desencriptar=crypt.desencriptar

#Ejemplos Validaciones

#print(valint(4)) #un solo argumento tipo int
#print(valint(4.0)) #un solo argumento pero es tipo float
#print(valint(4.0,[4,10])) #dos argumentos y el primero no es de tipo int
#print(valint(4,"a")) #dos argumentos y el segundo no es de tipo esperado, en este caso una lista o tupla 
#print(valint(4,[4,9])) #dos argumentos, el segundo es de tipo esperado y creciente, y el primero se encuentra en el intervalo del segundo
#print(valint(4,[10,4])) #dos argumentos, pero el segundo no es una lista o tupla creciente
#print(valint(4,(4,10))) #dos argumentos, pero el primero no se encuentra en el intervalo del segundo
#print(valint(4,5)) #dos argumentos y el segundo no es del tipo esperado 
#print(valint(4,[1,"a"])) #un elemento de la lista no es un entero 

#print(valfloat(4.0)) #un solo argumento tipo float
#print(valfloat(4)) #un solo argumento pero es tipo int
#print(valfloat(4,[4,10])) #dos argumentos y el primero no es de tipo float
#print(valfloat(4.0,"a")) #dos argumentos y el segundo no es de tipo esperado, en este caso lista o tupla
#print(valfloat(4.0,[4,9])) #dos argumentos, el segundo es de tipo esperado y creciente, y el primero se encuentra en el intervalo del segundo
#print(valfloat(4.0,(1,5.6))) #mismo caso pero con una tupla
#print(valint(4.0,(4,10))) #dos argumentos, pero el primero no se encuentra en el intervalo del segundo
#print(valfloat(4.0,[6,3.8])) #dos argumentos, pero el segundo no es una lista o tupla creciente
#print(valfloat(4.0,[1,"a"])) #un elemento de la lista no es un numero

#print(valcomplex(3+4j)) #un solo argumento tipo complex
#print(valcomplex(4.0)) #un solo argumento pero no es tipo complex
#print(valcomplex(4,[5,10])) #dos argumentos y el primero no es de tipo complex
#print(valcomplex(3+4j,"a")) #dos argumentos y el segundo no es de tipo esperado, en este caso lista o tupla
#print(valcomplex(3+4j,[5,10])) #dos argumentos, el segundo es de tipo esperado y el modulo del primero se encuentra en el intervalo del segundo
#print(valcomplex(3-4j,[5,10])) #mismo caso pero el modulo sin el valor absoluto da negativo
#print(valcomplex(3+4j,[10,4])) #dos argumentos, pero el segundo no es una lista creciente
#print(valint(3+4j,(5,10))) #dos argumentos, pero el primero no se encuentra en el intervalo del segundo
#print(valcomplex(3+4j,[4,"a"])) #un elemento de la lista no es un numero

#print(vallist(["a","b"])) #un solo argumento de tipo list
#print(vallist("a")) #un solo argumento pero no es una lista
#print(vallist(["a","b"],[1,2])) #dos argumentos
#print(vallist(["a","b"],["a","b"],1)) #tres argumentos y el tercero no es una cadena de texto
#print(vallist(["a","b"],["a","b"],"hola")) #tres argumentos, el tercero es una cadena de texto pero no dice ni "value" ni "len"
#print(vallist(["a","b"],["a","b"],'value')) #tres argumentos, los dos primeros son listas identicas y el tercero es "value"
#print(vallist(["a","b"],["c","b"],'value')) #tres argumentos, el tercero es "value" pero no son listas identicas
#print(vallist(["a","b"],["a","b"],'len')) #tres argumentos, el tercero es 'len' pero el segundo no es un entero
#print(vallist(["a","b"],4,'len')) #tres argumentos, el tercero es "len" pero la longitud del primero no coincide con el segundo argumento
#print(vallist(["a","b"],2,'len')) #tres argumentos, el tercero es 'len y la longitud del primero coincide con el segundo argumento


#Ejemplos Encriptado:

#print(encriptar('hay que votar el domingo')) #una frase para encriptar
#print(desencriptar('wpn fjt kdipg ta sdbxcvd')) #la misma frase desencriptada
#print(encriptar('hay que votar el domingo 28!!')) #una frase con caracteres fuera del alfabeto
#print(desencriptar('wpn fjt kdipg ta sdbxcvd 28!!')) #la misma frase desencriptada