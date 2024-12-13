#Nombre: Stefany Martinez Barco
#Fecha: 09 de Octubre de 2024
#Este programa pregunta cuantos numeros se van a introducir y dice cuantos de ellos son negativos:
print("NÚMEROS NEGATIVOS")
nu=eval(input("¿Cuántos valores va a introducir? "))
neg=0
if nu<0:
    print("¡Imposible!")
elif nu==0:
    print("No ha escrito ningún número negativo.")
else:
    for orden in range (1,nu+1):
        val=eval(input("Escriba el numero "+str(orden)+": "))
        if val<0:
            neg=neg+1
    if neg>1:
        print("Ha escrito", neg, "números negativos.")
    else:
        print("Ha escrito 1 número negativo.")