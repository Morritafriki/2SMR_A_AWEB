#Nombre: Stefany Martinez Barco
#Fecha: 12 de Octubre de 2024
#Este programa pide la anchura de un triangulo y lo dibuja con "*":
def triangulo ():
    anch=eval(input("Anchura del triángulo: "))
    for x in range(1,anch+1):
        print("* " * x )
    for x in range(anch,1,-1): 
        print("* " * (x-1) )
triangulo()