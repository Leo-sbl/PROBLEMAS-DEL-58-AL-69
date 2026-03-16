# PROBLEMAS 58 AL 60
#PROBLEMA 58
cantidad = int(input("¿cuantos numeros desea ingresar?"))
def llenar_lista () : 
    lista = []
    for i in range (cantidad) : 
        numero = int(input(f"ingrese el numero {i+1}:"))
        lista.append(numero)
    return lista 
lista = llenar_lista()
print ( "la lista es:" , lista ) 

#PROBLEMA 59
def sumar () :
    suma = 0
    for i in range (cantidad) :
     suma += lista[i]
    return suma 
suma = sumar()
print("la sumatoria es :" , suma)

#PROBLEMA 60
def promedio ():
   promedio = suma / cantidad 
   return promedio 
resultado = promedio()
print ("el promedio es :" , resultado)