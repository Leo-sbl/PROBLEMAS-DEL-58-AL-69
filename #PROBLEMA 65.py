#PROBLEMA 65
def factorial(n):
    if n < 0:
        return None  
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def programa():
    contador = 0
    while True:
        entrada = input("Ingrese un número  'fin' para terminar : ")
        if entrada.lower() == "fin":
            break
        try:
            numero = int(entrada)
            fact = factorial(numero)
            if fact is None:
                print(f"No existe factorial para {numero}")
            else:
                print(f"El factorial de {numero} es {fact}")
            contador += 1
        except ValueError:
            print("Entrada inválida, por favor ingrese un número entero.")

    print("Cantidad total de números leídos:", contador)
programa()