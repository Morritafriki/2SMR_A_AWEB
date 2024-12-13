#Nombre: Stefany Martinez Barco
#Fecha: 04 de Octubre de 2024
#Este programa pide dos números enteros y escribe una lista de los numeros consecutivos a ellos de menos a mayor:
print("LISTA DE MENOR A MAYOR")
n1=(eval(input("Escriba un número entero: ")))
n2=(eval(input("Escriba otro número entero: ")))
if n1<n2:
    n1=n1+1
    print(list(range(n1,n2)))
elif n1>n2:
    n2=n2+1
    print(list(range(n2,n1)))
else:
    print("[]")