#Nombre: Stefany Martinez Barco
#Fecha: 10 de Octubre de 2024
#Este programa pide numeros pares y mientras se le diga que si, va pidiendolos hasta que se le diga de parar, da como resultado la cantidad de numeros pares que se ha introducido:
print("CUENTA PARES (1)")
np=eval(input("Escriba un número par: "))
while np%2!=0:
    np=eval(input(str(np)+ " no es un número par. Inténtelo de nuevo: "))
totalp=1
Pregunta=input("¿Quiere escribir otro número par? (S/N): ")
while Pregunta=="S" or Pregunta=="s":
    np=eval(input("Escriba un número par: "))
    while np%2!=0:
        np=eval(input(str(np)+ " no es un número par. Inténtelo de nuevo: "))
    totalp=totalp+1
    Pregunta=input("¿Quiere escribir otro número par? (S/N): ")
if totalp==1:
    print("Ha escrito 1 número par.")
else:
    print("Ha escrito", totalp, "números pares.")