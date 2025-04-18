import random, math

'''
#1
for i in range(101):
    print(i)

#2
n = input("Ingrese un numero entero: ")
print(f"el total de digitos es:{len(n)}") 




#3
n1 = int(input("Ingrese un numero entero: "))
n2 = int(input("Ingrese otro numero entero: "))
suma = 0
if n1 < n2:
    for i in range(n1,n2+1):
       suma = suma + i;
else:
    for i in range(n2,n1+1):
        suma = suma + i
print(suma)



#4
n = int(input("Ingrese un numero entero: "))
suma = 0
while n != 0:
    suma = suma + n
    n = int(input("Ingrese un numero entero: "))
print(suma)


#5

numeros_aleatorios = random.randint(0,9)
n = int(input("Adivina el numero! (0 a 9):"))
cont = 0
while n != numeros_aleatorios:
    cont= cont+1
    print("Perdiste! Sigue intenando")
    n = int(input("Adivina el numero! (0 a 9):"))

print("Adivinaste!", numeros_aleatorios, n)
print("Intentos:", cont)
    


#6

for i in range(100,-1,-2):
    print(i)



#7

n = int(input("Ingrese un numero entero: "))
suma = 0
for i in range(0,n+1):
    suma = suma + i
print(suma)


#8 
par = 0
impar = 0
pos = 0
neg = 0

for i in range(5): #cambiar 5 por 100
    n = int(input("Ingresar 100 numeros enteros:"))
    
    if n % 2 == 0:
        par +=1
    else:
        impar +=1
    
    if n > 0:
        pos +=1
    else:
        neg +=1
  
print("par:",par)
print("impar:",impar)
print("positivo:",pos)
print("negativo:",neg)


suma = 0
for i in range(5): #cambiar 5 por 100
    n = int(input("Ingresar 100 numeros enteros:"))
    suma = suma + n
    media = suma / 5 #cambiar por 100

print(suma)
print(media)

'''

#10 
n = float(input("Ingrese un numero:"))
digito = 0
n_invertido = 0
while n > 0:
    digito = n % 10
    n_invertido = (n_invertido * 10) + digito
    n = n /10
print(n_invertido)





