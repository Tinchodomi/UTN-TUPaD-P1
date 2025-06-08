# Listas diferentes de vehículos para cada método
vehiculos_burbuja = [
    {"modelo": "Toyota Corolla", "año": 2010},
    {"modelo": "Honda Civic", "año": 2012},
    {"modelo": "Ford Focus", "año": 2008}
]

vehiculos_quick = [
    {"modelo": "Mazda", "año": 2011},
    {"modelo": "Chevrolet Cruze", "año": 2015},
    {"modelo": "Nissan Sentra", "año": 2009}
]

vehiculos_seleccion = [
    {"modelo": "Kia", "año": 2013},
    {"modelo": "Hyundai", "año": 2014},
    {"modelo": "Subaru Impreza", "año": 2010}
]

vehiculos_insercion = [
    {"modelo": "Volkswagen Golf", "año": 2012},
    {"modelo": "Mercedez Benz b250", "año": 2014},
    {"modelo": "Citroën C4", "año": 2009}
]

# Función de ordenamiento burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]['año'] > lista[j + 1]['año']:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Función de quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]['año']
    menores = [x for x in lista if x['año'] < pivote]
    iguales = [x for x in lista if x['año'] == pivote]
    mayores = [x for x in lista if x['año'] > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)

# Función de selección
def seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j]['año'] < lista[min_idx]['año']:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Función de inserción
def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j]['año'] > clave['año']:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Ordenar y mostrar en cada método con su lista específica
libros_burbuja = burbuja(vehiculos_burbuja)
libros_quick = quicksort(vehiculos_quick)
libros_seleccion = seleccion(vehiculos_seleccion)
libros_insercion = insercion(vehiculos_insercion)

# Mostrar resultados
print("Ordenados por burbuja:")
for v in libros_burbuja:
    print(f"{v['modelo']} ({v['año']})")

print("\nOrdenados por quicksort:")
for v in libros_quick:
    print(f"{v['modelo']} ({v['año']})")

print("\nOrdenados por selección:")
for v in libros_seleccion:
    print(f"{v['modelo']} ({v['año']})")

print("\nOrdenados por inserción:")
for v in libros_insercion:
    print(f"{v['modelo']} ({v['año']})")