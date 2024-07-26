def vallist(*args):
    arg_1=args[0]
    
    if len(args)==2:
        raise ValueError('Debe proporcionar uno o tres argumentos')
    if len(args)==1:
        if not isinstance(arg_1,list):
            return False
        return True
    if len(args)==3:
        arg_2=args[1]
        arg_3=args[2]
        if not isinstance(arg_3,str):
            raise TypeError('El tercer argumento debe ser una "cadena de texto"')
        if arg_3=='value':
            if not isinstance(arg_1,list):
                raise TypeError('El primer argumento debe ser una "lista"')
            if not isinstance(arg_2,list):
                raise TypeError('El segundo argumento debe ser de tipo "lista"')
            if arg_1!=arg_2:
                return False
        if arg_3=='len':
            if not isinstance(arg_1,list):
                raise TypeError('El primer argumento debe ser de tipo "lista"')
            if not isinstance(arg_2,int):
                raise TypeError('el segundo argumento debe ser de tipo "entero"')
            if len(arg_1)!=arg_2:
                return False
        if arg_3!='value' and arg_3!='len':
            raise ValueError('el tercer argumento solo puede recibir "value" o "len"')
    return True


def valfloat(*args):
    numero=args[0]
    if len(args)>2:
        raise ValueError('debe ingersar máximo dos argumentos')
    if len(args)==1:
        if not isinstance(numero,float):
            return False
        return True
    if len(args)==2:
        lista=args[1]
        if not isinstance(numero,float):
            return False
        if not isinstance(lista,(list, tuple)):
            raise TypeError('El segundo argumento debe ser una lista o tupla')
        if len(lista)!=2:
            raise ValueError('el segundo argumento debe contener exactamente dos elementos')
        for elemento in lista:
            if not isinstance(elemento,(int,float)):
                raise ValueError('La lista solo puede contener numeros')
        for lugar in range(1, len(lista)):
            if lista[lugar] <= lista[lugar - 1]:
                raise ValueError('La lista o tupla debe ser creciente')
        if (numero<min(lista) or numero>max(lista)) and isinstance(lista,list):
            return False
        if (numero<=min(lista) or numero>=max(lista)) and isinstance(lista,tuple):
            return False
        return True
    

def valint(*args):
    numero=args[0]
    if len(args)>2:
        raise ValueError('debe ingersar máximo dos argumentos')
    if len(args)==1:
        if not isinstance(numero,int):
            return False
        return True
    if len(args)==2:
        lista=args[1]
        if not isinstance(numero,int):
            return False
        if not isinstance(lista,(list,tuple)):
            raise TypeError('El segundo argumento debe ser una lista o tupla de enteros')
        if len(lista)!=2:
            raise ValueError('La lista debe contener exactamente dos elementos')
        for elemento in lista:
            if not isinstance(elemento,int):
                raise TypeError('Los elementos de la lista deben ser enteros')
        for lugar in range(1, len(lista)):
            if lista[lugar] <= lista[lugar - 1]:
                raise ValueError('La lista debe ser creciente')
        if (numero<min(lista) or numero>max(lista)) and isinstance(lista,list):
            return False
        if (numero<=min(lista) or numero>=max(lista)) and isinstance(lista,tuple):
            return False
        return True
    
    
import math
def valcomplex(*args):
    numero=args[0]
    if len(args)>2:
        raise ValueError('debe ingersar máximo dos argumentos')
    if len(args)==1:
        if not isinstance(numero,complex):
            return False
        return True
    if len(args)==2:
        lista=args[1]
        if not isinstance(numero,complex):
            return False
        if not isinstance(lista,(list,tuple)):
            raise TypeError('El segundo argumento debe ser una lista o tupla')
        if len(lista)!=2:
            raise ValueError('La lista debe contener exactamente dos elementos')
        for elemento in lista:
            if not isinstance(elemento,(int,float)):
                raise TypeError('Los elementos de la lista deben ser numeros')
        for lugar in range(1, len(lista)):
            if lista[lugar] <= lista[lugar - 1]:
                raise ValueError('La lista debe ser creciente')
        modulo=math.sqrt(numero.real**2+numero.imag**2)
        negativo=-modulo
        if modulo<0:
            if (negativo<min(lista) or negativo>max(lista)) and isinstance(lista,list):
                return False
            else: return True
        if modulo>=0:
            if (modulo<=min(lista) or modulo>=max(lista)) and isinstance(lista,tuple):
                return False
            else:
                return True
        return True