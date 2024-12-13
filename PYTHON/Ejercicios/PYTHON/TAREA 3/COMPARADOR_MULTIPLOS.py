#Nombre: Stefany Martinez Barco
#Fecha: 03 de Octubre de 2024
#Este programa pide dos numeros enteros y dice si el mayor es multiplo del menor, no admite 0, ni numeros negativos, como resultado da un aviso:
print("COMPARADOR DE MÚLTIPLOS")
n1=input("Escriba un número: ")
n2=input("Escriba otro número: ")
n1=eval(n1)
n2=eval(n2)
if n1 == 0 or n2 == 0:
    print("Lo siento, este programa no admite valores nulos.")
elif n1<0 or n2<0:
    print("Lo siento, este programa no admite valores negativos.")
elif n1>=n2 and n1%n2!=0:
    print(n1, "no es múltiplo de", n2)
elif n2>=n1 and n2%n1==0:
        print(n2, "es múltiplo de", n1)
elif n2>=n1 and n2%n1!=0:
        print(n2, "no es múltiplo de", n1)
else:
    print(n1, "es múltiplo de", n2)
