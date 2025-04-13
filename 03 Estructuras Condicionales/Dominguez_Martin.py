

#1
'''
edad = int(input("Ingrese su edad:"))
if edad >= 18:
    print("Es mayor de edad")


#2

nota = int(input("Ingrese su nota:"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3
par = int(input("Ingresar numero par:"))
if par % 2 == 0:
    print("Numero par")
else:
    print("Por favor ingrese un numero par")

edad = int(input("Ingrese su edad:"))
if edad < 12:
    print("Niño")
elif edad >= 12 and edad <18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/joven")
elif edad >= 30:
    print("Adulto")
else:
    print(" 0 o menos no es una edad")



#5 
contraseña = input("Ingrese una contraseña entre 8 y 14 caracteres:")
if len(contraseña) < 8 or len(contraseña) > 14:
    print("Por favor ingrese una contraseña entre 8 y 14 caracteres")
else:
    print("Ha ingresado na contraseña correcta")

    

#6

import random
from statistics import mode,median,mean

numeros_aleatorios = [random.randint(1,100) for i in range(50)]
print(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("moda: " , moda)
print("mediana: ", mediana)
print("media: " , media)

if media > mediana and mediana > moda:
    print("sesgo positivo")
elif media < mediana and mediana < moda:
    print("sesgo negativo")
elif media == mediana == moda:
    print("sin sesgo")
else:
    print("No se realizo sesgo")

#7

frase = input("Ingrese una frase o palabra:")
vocales = 'aeiou'

if frase[-1] in vocales:
    frase += "!"
    print(frase)
else:
    print(frase)



#8

nombre = input("Ingrese su nombre:")
opcion = int(input("Ingrese: \n1.Nombre en mayuscula \n2.Nombre en minuscula \n3.Nombre con la primer letra mayuscula \nOpcion:"))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())



#9

magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >=3 and magnitud < 4:
    print("Leve")
elif magnitud >=4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >=6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

'''
#10

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()  
mes = int(input("¿Qué mes del año es?: "))  
dia = int(input("¿Qué día es?: "))  

 
if hemisferio == 'N':  
    if (mes == 3 and dia >= 20) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):  
        estacion = "Primavera"  
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 23):  
        estacion = "Verano"  
    elif (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):  
        estacion = "Otoño"  
    else:  
        estacion = "Invierno"  
elif hemisferio == 'S':  
    if (mes == 3 and dia >= 20) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):  
        estacion = "Otoño"  
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 23):  
        estacion = "Invierno"  
    elif (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):  
        estacion = "Primavera"  
    else:  
        estacion = "Verano"  
else:  
    estacion = "Hemisferio no válido"  

# Imprimir el resultado  
print(f"En el hemisferio {hemisferio}, la estación es: {estacion}.")  

     














