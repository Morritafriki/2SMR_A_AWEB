#Nombre: Stefany Martinez Barco
#Fecha: 04 de Octubre de 2024
#Este programa pide un numero entero mayor que cero y te dice los divisores de este:
print("DIVISORES")
n=eval(input("Escriba un número mayor que cero: "))
if n<0:
    print("¡Le he pedido un número entero mayor que cero!")
else:
    print("Los divisores de", n, "son", end=" ")
    for div in range (1,n+1):
        if n%div== 0:
            print(div,end=" ")