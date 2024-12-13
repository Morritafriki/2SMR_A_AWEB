#Nombre: Stefany Martinez Barco
#Fecha: 12 de Octubre de 2024
#Este programa pide la anchura y altura de un rectangulo y segun esto lo dibuja con "*":
def rectangulo():
    anch=eval(input("Anchura del rectángulo: "))
    alt=eval(input("Altura del rectángulo: "))
    for x in range(alt):
        for y in range (anch+1):
            if y==anch:
                print ()
            else:
                print (end="* ")
rectangulo()