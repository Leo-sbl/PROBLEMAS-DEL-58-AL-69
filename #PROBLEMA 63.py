#PROBLEMA 63
lista = [1, 2, 3, 4, 5]
def cuadrados(lista):
    nueva_lista = []
    for numero in lista:
        nueva_lista.append(numero ** 2)
    return nueva_lista
resultado = cuadrados(lista)
print("Lista original:", lista)
print("Lista de cuadrados:", resultado)