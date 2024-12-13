#Nombre: Stefany Martinez Barco
#Fecha: 03 de Octubre de 2024
#Este programa pide un año y dice si es bisiesto o no:
print("COMPROBADOR DE AÑOS BISIESTOS")
año=input("Escriba un año y le diré si es bisiesto: ")
año=eval(año)
if año%4==0:
    if año%100==0:
        if año%400==0:
            print("El año",año,"es un año bisiesto porque es mÚltiplo de 400.")
        else:
         print("El año",año,"no es un año bisiesto porque es múltiplo de 100 sin ser múltiplo de 400.")
    else:
        print("El año",año,"es un año bisiesto porque es múltiplo de 4 sin ser múltiplo de 100.")
else:
    print("El año",año,"no es un año bisiesto.")