#Nombre: Stefany Martinez Barco
#Fecha: 02 de Octubre de 2024
#Este programa pide un numero par y si no es correcto mostrara un aviso, si es correcto pedira un numero impar y si este no es correcto mostrara otro aviso.
print("PAR E IMPAR (2)")
PAR = input("Escriba un número par: ")
PAR=eval(PAR)
if PAR%2==0:
    IMPAR = input("Escriba un número impar: ")
    IMPAR=eval(IMPAR)
    if IMPAR%2==1:
        print("¡Gracias por tu colaboración!")
    else:
        print("No se ha escrito un numero impar.")
        print("Ejecute de nuevo el programa para volver a intentarlo.")
else:
    print("No se ha escrito un numero par.")
    print("Ejecute de nuevo el programa para volver a intentarlo.")

