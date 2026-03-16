#PROBLEMA 61
def perimetro ():
    base = float(input("ingrese la base de su retangulo:"))
    altura = float(input("ingrese la altura de su retangulo:"))
    resultado = (base * altura)
    return resultado
resultado = perimetro ()
print("el perimetro es:" , resultado )