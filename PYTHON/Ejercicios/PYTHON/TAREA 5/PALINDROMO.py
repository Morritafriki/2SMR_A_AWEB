#Nombre: Stefany Martinez Barco
#Fecha: 12 de Octubre de 2024
#Este programa te dice si una frase es palindroma o no:
def palindromo():
    fraseoriginal=input("Dígame algo: ")
    palabraoriginallista=[]
    originalsinespacios=[]
    reversasinespacios=[]
    for x in range (0, len(fraseoriginal)):
        palabraoriginallista.append(fraseoriginal[x])
    for x in range (len(palabraoriginallista)):
        if palabraoriginallista[x] != " ":
            originalsinespacios.append(palabraoriginallista[x])
    for x in range (len(originalsinespacios)-1,-1,-1):
        reversasinespacios.append(originalsinespacios[x])
    if reversasinespacios==originalsinespacios:
        print(fraseoriginal, "es palíndroma")
    else:
        print(fraseoriginal, "no es palíndroma") 
palindromo()