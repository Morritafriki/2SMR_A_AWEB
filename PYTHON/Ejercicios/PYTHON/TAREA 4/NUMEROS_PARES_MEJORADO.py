#Nombre: Stefany Martinez Barco
#Fecha: 10 de Octubre de 2024
#Este programa mejora el anterior sin parar si es que no se escribe explicitamente n o N:
print("CUENTA PARES (2)")
np=eval(input("Escriba un número par: "))
while np%2!=0:
    np=eval(input(str(np)+ " no es un número par. Inténtelo de nuevo: "))
totalp=1
Pregunta=input("¿Quiere escribir otro número par? (S/N): ") 
while Pregunta!="S" and Pregunta!="s"  and Pregunta!="N" and Pregunta!="n":
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