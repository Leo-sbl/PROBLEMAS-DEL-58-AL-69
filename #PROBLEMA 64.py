#PROBLEMA 64
a = int(input("ingrese el primer numero:"))
b =  int(input("ingrese el segundo numero:"))
def Multiplo(a, b):
    if b == 0:
        return False  
    return a % b == 0
if Multiplo(a, b):
    print(f"{a} es múltiplo de: {b}")
else:
    print(f"{a} NO es múltiplo de: {b}")