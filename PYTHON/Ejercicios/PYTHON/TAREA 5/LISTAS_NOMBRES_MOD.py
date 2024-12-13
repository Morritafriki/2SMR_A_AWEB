#Nombre: Stefany Martinez Barco
#Fecha: 12 de Octubre de 2024
#Este programa mejora el anterior escribiendo las listas al final:
def generador_listas():
    print("Generador de listas")
    nlistas=eval(input("¿Cuántas listas quiere escribir? "))
    print()
    listatotal=[]
    for orden in range(1,nlistas+1):
        lista=eval(input("Dígame cuántas palabras tiene la lista "+ str(orden)+": "))
        listanombre=[]
        for orden2 in range(1,lista+1):
            palabra=input("Dígame la palabra "+ str(orden2)+": ")
            listanombre.append(palabra)
        print()
        listatotal.append(listanombre)
    for x in range(len(listatotal)):
        print("La lista", x+1, "es: ", listatotal[x])
generador_listas()