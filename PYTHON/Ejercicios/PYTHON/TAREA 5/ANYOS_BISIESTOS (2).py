#Nombre: Stefany Martinez Barco
#Fecha: 12 de Octubre de 2024
#Este programa pide dos años y dice cuantos años hay entre estas dos fechas, asi como cuantos de estos son bisiestos:
print("CONTADOR DE AÑOS BISIESTOS")
def bisiesto ():
    año1=eval(input("Escriba un año: "))
    año2=eval(input("Escriba otro año posterior a "+ str(año1) +": "))
    while año2<año1:
        año2=eval(input(str(año2)+ " no es mayor que "+ str(año1)+". Inténtelo de nuevo: "))
    totalaños=(año2-año1)+1
    bisiesto=0
    for x in range(año1,año2+1):
        if x%4==0 and x%100!=0:
            bisiesto=bisiesto+1
        elif x%4==0 and x%100==0 and x%400==0:
                    bisiesto=bisiesto+1
        else:
              bisiesto=bisiesto
    print("De", año1, "a", año2, "hay", totalaños,"años,", bisiesto, "de ellos bisiestos.")

bisiesto()