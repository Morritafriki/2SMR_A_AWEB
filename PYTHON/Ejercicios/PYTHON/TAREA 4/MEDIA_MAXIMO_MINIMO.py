#Nombre: Stefany Martinez Barco
#Fecha: 09 de Octubre de 2024
#Este programa pide la cantidad de valores que se van a introducir y te dice cual es el minimo, el maximo y la media:
print("MAYOR, MENOR Y MEDIA ARITMÉTICA")
val=eval(input("¿Cuántos valores va a introducir? "))
if val<0:
    print("¡Imposible!")
else:
    num=eval(input("Escriba el número 1: "))
    minimo=maximo=suma=num
    for orden in range (2,val+1):
        num=eval(input("Escriba el numero "+str(orden)+": "))
        suma=suma+num
        if num<minimo:
            minimo=num
        if num>maximo:
            maximo=num
    print("El número más pequeño de los introducidos es", minimo)
    print("El número más grande de los introducidos es", maximo)
    print("La media de los números introducidos es", suma/val)