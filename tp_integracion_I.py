#Alumno: DOMINGUEZ MARTIN

#Simulación de Puertas Lógicas Básicas:
#Programa en Python que simule las puertas AND, OR y NOT. 
#Soliciten al usuario ingresar valores binarios (0 o 1) y muestren el resultado de cada operación.

while True:
        print("\nMenú de Compuertas Lógicas")
        print("1. AND")
        print("2. OR")
        print("3. NOT")
        print("4. SALIR")
        opcion = input("Selecciona una opción : ")

# Solicitar valores para la puerta AND  
        if opcion == '1':
                a_and = int(input("Ingrese el primer valor (0 o 1) para AND: "))  
                b_and = int(input("Ingrese el segundo valor (0 o 1) para AND: "))  

# Validar entrada para AND  
                while a_and > 1 or a_and < 0 or b_and > 1 or b_and < 0:
                        print("Valor no válido. Debe ser 0 o 1.")
                        a_and = int(input("Ingrese el primer valor (0 o 1) para AND: "))  
                        b_and = int(input("Ingrese el segundo valor (0 o 1) para AND: "))

# Operación AND  
                resultado_and = a_and & b_and  
                print(f"Resultado AND: {resultado_and}") 
    
# Solicitar valores para la puerta OR 
        elif opcion == '2':
                a_or = int(input("\nIngrese el primer valor (0 o 1) para OR: "))  
                b_or = int(input("Ingrese el segundo valor (0 o 1) para OR: "))  

# Validar entrada para OR 
                while a_or > 1 or a_or < 0 or b_or > 1 or b_or < 0: 
                        print("Valor no válido. Debe ser 0 o 1.") 
                        a_or = int(input("\nIngrese el primer valor (0 o 1) para OR: "))  
                        b_or = int(input("Ingrese el segundo valor (0 o 1) para OR: "))   
       
# Operación OR  
                resultado_or = a_or | b_or 
                print(f"Resultado OR: {resultado_or}")  
        elif opcion == '3':
# Solicitar valor para la puerta NOT  
                a_not = int(input("\nIngrese el valor (0 o 1) para NOT: "))  

# Validar entrada para NOT 
                while a_not > 1 or a_not < 0: 
                        print("Valor no válido. Debe ser 0 o 1.")
                        a_not = int(input("\nIngrese el valor (0 o 1) para NOT: "))   
  
# Operación NOT  
                resultado_not = 1 - a_not 
                print(f"Resultado NOT: {resultado_not}") 
        
        elif opcion == '4':
                print("Salio del sistema")
                break

        else:
                
                print("Opción inválida, intenta de nuevo.")

                

