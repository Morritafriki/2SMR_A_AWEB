#Nombre: Stefany Martinez Barco
#Fecha: 12 de Octubre de 2024
#Este programa pide cuantas listas se quiere crear y las solicita y te las muestra:
def generador_listas():
    print("Generador de listas")
    nlistas=eval(input("¿Cuántas listas quiere escribir? "))
    print()
    for orden in range(1,nlistas+1):
        lista=eval(input("Dígame cuántas palabras tiene la lista "+ str(orden)+": "))
        listanombre=[]
        for orden2 in range(1,lista+1):
            palabra=input("Dígame la palabra "+ str(orden2)+": ")
            listanombre.append(palabra)
        print("La lista", orden, "es:", listanombre)
        print()
generador_listas()