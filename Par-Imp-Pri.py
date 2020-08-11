#Presentador de n primeros numeros Pares, Impares y Primos
#Author: Kevin Alexander Puentes Yaya
#10/08/2020




def par(x):#funcion de identificacion de pares
    if x%2==0:
        return True
    return False

def impar(x):#funcion de identificacion de numeros impares
    if x%2>=1:
        return True
    return False

def primo(x): #funcion para identificar primos
    if x==2: #nos aseguramos del primer primo
        return True

    if x%2==0: #si su modulo es igual a 0 no es un primo
        return False

    i=3  

    while i**2<=x: #nos aseguramos de los multiplos de valores no pares
        if x%i==0:
            return False
        i=i+2
    return True

x=input("Ingrese un numero: ")

print("------------PARES------------")

c=2
contador=1


while contador<=x:#evaluacion de los primeros n numeros pares
    if par(c):
        print str(contador)+ ") " + str(c)
        contador+=1
    c+=1

print("------------IMPARES------------")

c=1
contador=1


while contador<=x:#evaluacion de los primeros n numeros impares
    if impar(c):
        print str(contador)+ ") " + str(c)
        contador+=1
    c+=1

print("------------PRIMOS------------")

c=2
contador=1

while contador<=x:#evaluacion de los primeros n numeros primos
    if primo(c):
        print str(contador)+ ") " + str(c)
        contador+=1
    c+=1
    

 


