#Nombre: Stefany Martinez Barco
#Fecha: 02 de Octubre de 2024
#Este programa pide tres números y te dice si son iguales, si hay dos iguales o si son todos diferentes.
print("COMPARADOR DE TRES NÚMEROS")
n1=input("Escriba un número: ")
n2=input("Escriba otro número: ")
n3=input("Escriba otro número más: ")
n1=eval(n1)
n2=eval(n2)
n3=eval(n3)
if n1 == n2 and n2 == n3:
    print("Ha escrito tres veces el mismo número.")
elif n1==n2 or n2==n3 or n1==n3:
    print("Ha escrito uno de los números dos veces.")
else:
    print("Los tres números que ha escrito son distintos.")
 

   
