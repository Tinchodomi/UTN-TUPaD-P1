'''
#1
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)
    
n = int(input("Ingrese un numero para calcular el su factorial:"))
print(fact(n))

#2
def fibon(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibon(pos -1) + fibon(pos -2)
    
n = int(input("Ingrese la posicion de la serie de fibonacci:"))
print(fibon(n))

#3
def potencia(n,m):
    resultado = (n * n**(m-1))
    return resultado

print(potencia(4,3))


def decimal_a_binario(n):
    if n <= 1:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n%2)
    
n = 10
print(decimal_a_binario(n))

#5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
   
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1:-1])

#6
def suma_digitos(n):
        if n < 10:
             return n
        else:
            return (n%10) + suma_digitos(n // 10 )


def contar_bloques(n):
      if n <= 1:
            return 1
      else:
            return n + contar_bloques(n-1)
      

print(contar_bloques(4))

def contar_digito(n, d):
        if n <= 0:
            return 0
        elif d == n % 10: # comparo el digito con el decimal del numero
                cont = 1 #creo un contador para sumar la cantidad de digitos
                cont+1 # sumo la cantidad de digitos repetidos
                return cont + contar_digito(n//10,d)  # sumo el contador y llamo a la funcion para que repita la operacion
        else:
              return contar_digito((n//10),d) # si el digito no esta, llamo a la funcion restando ese digito hasta llegar a 0


print(contar_digito(1131132211,1))
              
'''