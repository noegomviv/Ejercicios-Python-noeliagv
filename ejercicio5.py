# coding=utf-8
__Author__="José Gaspar Sánchez García"

import random

# Función que determina si un numero es par.

def esPar(numero) :
    resto = (numero % 2)
    if resto == 0:
        return True # --> Implemente código de la función <--
    else:
        return False

def esImpar(numero) :
    resto = (numero % 2)
    if resto !=0:
        return True # --> Implemente código de la función <--
    else:
        return False
   # --> Implemente código de la función <--


#por aqui voy :()
def generarPares(valores, inicio) :
    pares=[]
    numero=inicio
    contador=valores
    while contador > 0 :
        if esPar(numero) :
            pares.append(numero)
            numero=numero+2
            contador=contador-1
        else :
            numero=numero+1   
    # --> Complete código de la función <--

    return pares

def generarImpares(valores, inicio) :
    impares=[]
    numero=inicio
    contador=valores
    while contador > 0 :
        if esImpar(numero) :   
            impares.append(numero)
            numero=numero+2
            contador=contador-1
        else :
            numero=numero+1
    # --> Complete código de la función <--
    
    return impares


# Programa principal
def main():
    print("Par e impar")
    n=int(input("Introduzca un numero: "))
    print("{0} es par --> {1}.".format(n,esPar(n)))
    m=int(input("Introduzca el número de valores: "))
    i=int(input("Introduzca el número inicial: "))
    x=generarPares(m,i)
    y=generarImpares(m,i)
    print("Impares: ",y)
    print("Pares: ",x)    

if __name__== "__main__" :
   main()
