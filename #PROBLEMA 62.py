#PROBLEMA 62
calif_1 = float(input("ingrese la primera calificacion:"))
calif_2  = float(input("ingrese la segunda  calificacion:"))
calif_3 = float(input("ingrese la tercera  calificacion:"))
def promedio (C1 , C2 , C3 ):
    suma = 0
    suma = calif_1 + calif_2 + calif_3
    resultado = suma/3
    if resultado <= 7.0 :
        print(f"tu promedio es de: {resultado} , te vas a extras")
    else : 
       print("tu resultado es de:")
    return resultado
final = promedio(C1= calif_1 , C2=calif_2, C3=calif_3)
print (final)
