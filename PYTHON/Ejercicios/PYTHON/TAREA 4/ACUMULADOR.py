#Nombre: Stefany Martinez Barco
#Fecha: 09 de Octubre de 2024
#Este programa pide dos numeros enteros y escribe la suma de todos los enteros desde el primer número hasta el segundo:
print("SUMA ENTRE VALORES")
NP=eval(input("Escriba un número entero positivo: "))
if NP<0:
    print("¡Le he pedido un número entero positivo!")
else:
    NM=eval(input("Escriba un número entero mayor que "+ str(NP)+": "))
    if NM==NP:
        print("¡Le he pedido un número entero mayor que", NP,"!")
    else:
        suma=0
        for s in range(NP,NM):
                suma=suma+s
        print("La suma desde", NP, "hasta", NM, "es" ,suma+NM)    