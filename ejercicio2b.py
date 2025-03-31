# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir. ok
# Implemente función esMayorEdad(e) --> falta
def esMayorEdad(e):
    if e >= 18:
        return True
    else :
        return False
    
# Programa principal
    # Utilice la función definida
    # Estructura alternativa Si (condidición con función) entonces --> sino ...
def main():
    nombre=input("Introduzca su nombre: ")
    edad=int(input(f"Introduzca su edad {nombre}: "))

    # Comprobamos si es mayor de edad - Estructura condicional if - else
    # Si edad mayor o igual a dieciocho --> Usted es mayor de edad
    # Sino --> Todavía eres menor de edad
    
    if esMayorEdad(edad):
        print("Usted es mayor de edad, ya puede conducir.")
    else:
        print("Todavía eres menor de edad")

if __name__== "__main__" :
   main()
