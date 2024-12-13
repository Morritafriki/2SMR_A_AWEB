#Nombre: Stefany Martinez Barco
#Fecha: 02 de Octubre de 2024
#Este programa divide dividendo entre divisor y da un mensaje con el resultado, diciendo si la division es exacta o no, mejora el anterior haciendo que se tenga en cuenta que no se puede dividir por 0.
print("DIVISOR DE NÚMEROS")
DIVE=input("Escriba el dividendo: ")
DIV=input("Escriba el divisor: ")
DIV=eval(DIV)
DIVE=eval(DIVE)
if DIV == 0:
    print("No se puede dividir por cero.")
elif DIVE%DIV == 0:
    print("La división es exacta. Cociente:", DIVE//DIV)
else:
    print("La división no es exacta. Cociente:", DIVE//DIV, "Resto:", DIVE%DIV)

