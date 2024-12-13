#Nombre: STEFANY MARTINEZ BARCO 
#Fecha: 30/09/2024
#Este pograma convertira los segundos que se introduzcan en cuantos minutos y segundos son:
print("CONVERTIDOR DE SEGUNDOS A MINUTOS")
SEG=input("Escriba una cantidad de segundos: ")
S=eval(SEG)
MIN=S//60
RESTO=S%60
print(SEG, "segundos son ", (MIN), "minutos y ",RESTO, "segundos" )