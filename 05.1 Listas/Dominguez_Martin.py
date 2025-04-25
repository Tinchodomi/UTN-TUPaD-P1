#1
mi_lista = list(range(4,101,4))
#print(mi_lista)

#2
mi_lista = [1,"hola",True, 1.5,["River","Campeon"]]
#print(mi_lista[-2])

#3
lista_vacia = []

hola = "Hola Mundo"
lista_vacia.append(hola)
#print(lista_vacia)

#4
animales = ["perro", "gato", "conejo", "pez"]
animales[1]= "loro"
animales[-1]= "oso"
#print(animales)

#5
numeros = [8,15,3,22,7]
numeros.remove(max(numeros)) #la funcion max recorre la lista buscando el maximo numero dentro de la lista ,luego remove lo elimina de la lista
#print(numeros)

#6
lista =list(range(10,31,5))
#print(lista[0:2])

#7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "peugeot"
autos[2] = "bmw"
#print(autos)

#8
dobles = []
elementos = [10,15,30] 
dobles.append(elementos)
#print(dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
#print(compras)

#10

lista_anidada = [15, True, [25.5,57.9,30.6], False]
print(lista_anidada)