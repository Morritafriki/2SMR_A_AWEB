#Nombre: Stefany Martinez Barco
#Fecha: 10 de Octubre de 2024
#Este programa pide la cantidad de numeros positivos que se van a escribir y pide numeros hasta que se hayan escrito todos los que pide, te indica la cantidad de numeros positivos que has escrito:
print("NÚMEROS POSITIVOS")
positivo=eval(input("Escriba la cantidad de números positivos a escribir: "))
while positivo<1:
    positivo=eval(input("La cantidad debe ser mayor que 0. Inténtelo de nuevo: "))
num=eval(input("Escriba un número: "))
tnum=1
if num>0:
    cant=1
else:
    cant=0
while cant<positivo:
    num=eval(input("Escriba otro número: "))
    if num>0:
        cant=cant+1
    tnum=tnum+1
if tnum == 1 and cant==1 and positivo==1:
    print("Ha escrito 1 número positivo.")
elif positivo == 1 and cant==1:
    print("Ha escrito", tnum ,"números", positivo, "de ellos positivo.")
else:
    print("Ha escrito", tnum ,"números", positivo, "de ellos positivos.")