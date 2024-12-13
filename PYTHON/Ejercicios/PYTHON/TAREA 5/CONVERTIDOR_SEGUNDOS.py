#Nombre: Stefany Martinez Barco
#Fecha: 12 de Octubre de 2024
#Este programa pide dias, horas, minutos y segundos y calcula cuantos segundos son en total:
def segundos():
    print("Convertidor a segundos")
    dias=eval(input("Dígame un número de días: "))
    dias1=dias*86400
    horas=eval(input("Dígame un número de horas: "))
    horas1=horas*3600
    minutos=eval(input("Dígame un número de minutos: "))
    minutos1=minutos*60
    segundos=eval(input("Dígame un número de segundos: "))
    total=dias1+horas1+minutos1+segundos
    print(dias, "días,", horas, "horas,", minutos, "minutos y", segundos, "segundos son",total,"segundos")
segundos()