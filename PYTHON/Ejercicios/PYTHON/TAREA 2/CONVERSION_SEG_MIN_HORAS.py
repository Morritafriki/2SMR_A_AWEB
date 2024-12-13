#Nombre: STEFANY MARTINEZ BARCO 
#Fecha: 02/10/2024
#Este pograma convertira los segundos que se introduzcan en cuantas horas, minutos y segundos son
print("CONVERTIDOR DE SEGUNDOS A MINUTOS")
SEG=input("Escriba una cantidad de segundos: ")
S=eval(SEG)
HORAS=S//3600
RESTOMIN=S%3600
MIN=RESTOMIN//60
RESTOSEG=RESTOMIN%60
print(SEG, "segundos son ", (HORAS), "horas", (MIN), "minutos y ",RESTOSEG, "segundos" )