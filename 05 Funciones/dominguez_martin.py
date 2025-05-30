import math
pi = math.pi

'''
#1
def imprimir_hola_mundo():
    return print("Hola Mundo!")

imprimir_hola_mundo()

#2

def saludar_usuario(nombre):
    return print("Hola", nombre)

saludar_usuario("Marcos")

#3
def informacion_personal(nombre,apellido,edad,residencia):
    
    return print("Soy", nombre, apellido, "tengo ", edad,"años y vivo en ", residencia)

nombre = input("Ingrese nombre:")
apellido = input("Ingrese apellido:")
edad = input("Ingrese edad:")
residencia = input("Ingrese residencia:")

informacion_personal(nombre,apellido,edad,residencia)

#4

def calcular_area_circulo(radio):
    area =  pi * pow(2, radio)
    return area

def calcular_perimetro_circulo(radio):
        perimetro = 2 * pi * radio
        return perimetro

radio = int(input("Ingrese el radio"))
print(f"El area es {calcular_area_circulo(radio)} y el perimetro es{calcular_perimetro_circulo(radio)}")



#5

def segundos_a_horas(segundos):
    horas = 3600
    resultado = segundos / horas
    return resultado
 
segundos = int(input("Ingresar segundos:"))
print(segundos_a_horas(segundos))


#6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print( numero,"x", i, "=",numero * i)

numero = int(input("Ingrese un numero:"))
tabla_multiplicar(numero)


#7

def operaciones_basicas(a,b):
    suma = a+b
    resta = a-b
    multi = a*b
    divi = a/b
    resultados = (suma,resta,multi,divi)
    return resultados

n1 = int(input("Ingrese primer numero:"))
n2 = int(input("Ingrese segundo numero:"))
print(operaciones_basicas(n1,n2))



def calcular_imc(peso,altura):
    imc = peso / altura**2
    return imc

peso = float(input("Ingrese su peso en kilogramos:"))
altura = float(input("Ingrese su altura en centimetros:"))
print(calcular_imc(peso,altura))


def celsius_a_fahenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

celsius = int(input("Ingrese los Grados Celsius: "))
print(celsius_a_fahenheit(celsius))


def calcular_promedio(a,b,c):
    resultado = (a+b+c)/3
    return resultado


n1 = int(input("Ingrese primer numero:"))
n2 = int(input("Ingrese segundo numero:"))
n3 = int(input("Ingrese tercer numero:"))
print(calcular_promedio(n1,n2,n3))
'''

