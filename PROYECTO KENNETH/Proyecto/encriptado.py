def encriptar(arg):
    if not isinstance(arg,str):
        raise TypeError('Debe ingresar una cadena de texto para encriptar')
    abc='abcdefghijklmnopqrstuvwxyz'
    cab='pqrstuvwxyzabcdefghijklmno'
    arg_cifrado=''
    for letra in arg.lower():
        if letra in abc:
            posicion=abc.index(letra)
            letra_cifrada=cab[posicion]
            arg_cifrado+=letra_cifrada
        else:
            arg_cifrado+=letra
    return arg_cifrado


def desencriptar(arg):
    if not isinstance(arg,str):
        raise TypeError('Debe ingresar una cadena de texto para encriptar')
    abc='abcdefghijklmnopqrstuvwxyz'
    cab='pqrstuvwxyzabcdefghijklmno'
    arg_descifrado=''
    for letra in arg.lower():
        if letra in cab:
            letra_descifrada=abc[cab.index(letra)]
            arg_descifrado+=letra_descifrada
        else:
            arg_descifrado+=letra
    return arg_descifrado


