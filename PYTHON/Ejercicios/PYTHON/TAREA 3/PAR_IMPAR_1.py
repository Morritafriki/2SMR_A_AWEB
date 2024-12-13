#Nombre: Stefany Martinez Barco
#Fecha: 02 de Octubre de 2024
#Este programa solicita un numero par y  otro impar y en caso de que uno no sea correcto muestra un aviso.
print("PAR E IMPAR (1)")
PAR = input("Escriba un número par: ")
IMPAR = input("Escriba un número impar: ")
PAR=eval(PAR)
IMPAR=eval(IMPAR)
if PAR % 2 == 0 and IMPAR % 2 == 1:
        print("¡Gracias por su colaboración!")
else:
    print("Uno o más de los valores que ha escrito no son correctos.")
    print("Ejecute de nuevo el programa para volver a intentarlo.")
    